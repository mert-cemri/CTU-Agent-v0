# Copyright Sierra

from typing import List, Dict, Any
from tau_bench.sft_types import SFTConversation, SFTDataset
from tau_bench.sft_utils import calculate_conversation_quality_score, analyze_dataset_diversity


class SFTQualityAssessor:
    """Assess quality of SFT datasets and individual conversations"""
    
    def __init__(self, quality_threshold: float = 0.7):
        self.quality_threshold = quality_threshold
    
    def assess_conversation(self, conversation: SFTConversation) -> Dict[str, Any]:
        """Assess quality of a single conversation"""
        quality_score = calculate_conversation_quality_score(conversation)
        
        return {
            "conversation_id": conversation.conversation_id,
            "quality_score": quality_score,
            "passes_threshold": quality_score >= self.quality_threshold,
            "success": conversation.success,
            "num_turns": conversation.num_turns,
            "num_tool_calls": conversation.num_tool_calls,
            "domain": conversation.domain,
            "agent_strategy": conversation.agent_strategy,
            "user_strategy": conversation.user_strategy,
            "quality_breakdown": self._get_quality_breakdown(conversation)
        }
    
    def assess_dataset(self, dataset: SFTDataset) -> Dict[str, Any]:
        """Assess quality of entire dataset"""
        if not dataset.conversations:
            return {"error": "Empty dataset"}
        
        # Assess individual conversations
        conversation_assessments = [
            self.assess_conversation(conv) for conv in dataset.conversations
        ]
        
        # Calculate aggregate metrics
        quality_scores = [assessment["quality_score"] for assessment in conversation_assessments]
        high_quality_conversations = [
            assessment for assessment in conversation_assessments 
            if assessment["passes_threshold"]
        ]
        
        # Diversity analysis
        diversity_metrics = analyze_dataset_diversity(dataset.conversations)
        
        # Strategy performance analysis
        strategy_performance = self._analyze_strategy_performance(conversation_assessments)
        
        return {
            "dataset_summary": {
                "total_conversations": len(dataset.conversations),
                "high_quality_conversations": len(high_quality_conversations),
                "quality_pass_rate": len(high_quality_conversations) / len(dataset.conversations),
                "average_quality_score": sum(quality_scores) / len(quality_scores),
                "min_quality_score": min(quality_scores),
                "max_quality_score": max(quality_scores)
            },
            "diversity_metrics": diversity_metrics,
            "strategy_performance": strategy_performance,
            "conversation_assessments": conversation_assessments,
            "recommendations": self._generate_recommendations(conversation_assessments, diversity_metrics)
        }
    
    def filter_high_quality_conversations(self, conversations: List[SFTConversation]) -> List[SFTConversation]:
        """Filter conversations that meet quality threshold"""
        high_quality = []
        
        for conv in conversations:
            assessment = self.assess_conversation(conv)
            if assessment["passes_threshold"]:
                high_quality.append(conv)
        
        return high_quality
    
    def _get_quality_breakdown(self, conversation: SFTConversation) -> Dict[str, Any]:
        """Get detailed quality breakdown for a conversation"""
        breakdown = {}
        
        # Success component
        breakdown["success_score"] = 30.0 if conversation.success else 0.0
        
        # Turn count component
        if 5 <= conversation.num_turns <= 20:
            breakdown["length_score"] = 20.0
        elif 3 <= conversation.num_turns <= 30:
            breakdown["length_score"] = 15.0
        elif conversation.num_turns >= 3:
            breakdown["length_score"] = 10.0
        else:
            breakdown["length_score"] = 0.0
        
        # Tool usage component
        if conversation.num_tool_calls > 0:
            breakdown["tool_usage_score"] = 15.0
            if conversation.num_tool_calls >= 3:
                breakdown["tool_usage_score"] += 10.0
        else:
            breakdown["tool_usage_score"] = 0.0
        
        # Content quality component (simplified)
        if conversation.turns:
            user_turns = len([t for t in conversation.turns if t.role == "user"])
            assistant_turns = len([t for t in conversation.turns if t.role == "assistant"])
            if user_turns >= 2 and assistant_turns >= 2:
                breakdown["content_score"] = 25.0
            elif user_turns >= 1 and assistant_turns >= 1:
                breakdown["content_score"] = 15.0
            else:
                breakdown["content_score"] = 5.0
        else:
            breakdown["content_score"] = 0.0
        
        breakdown["total_score"] = sum(breakdown.values())
        breakdown["normalized_score"] = min(breakdown["total_score"] / 100.0, 1.0)
        
        return breakdown
    
    def _analyze_strategy_performance(self, assessments: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze performance by strategy combinations"""
        strategy_stats = {}
        
        for assessment in assessments:
            agent_strategy = assessment["agent_strategy"]
            user_strategy = assessment["user_strategy"]
            domain = assessment["domain"]
            
            key = f"{domain}_{agent_strategy}_{user_strategy}"
            
            if key not in strategy_stats:
                strategy_stats[key] = {
                    "count": 0,
                    "quality_scores": [],
                    "success_count": 0,
                    "high_quality_count": 0
                }
            
            stats = strategy_stats[key]
            stats["count"] += 1
            stats["quality_scores"].append(assessment["quality_score"])
            if assessment["success"]:
                stats["success_count"] += 1
            if assessment["passes_threshold"]:
                stats["high_quality_count"] += 1
        
        # Calculate aggregated metrics
        for key, stats in strategy_stats.items():
            stats["avg_quality"] = sum(stats["quality_scores"]) / len(stats["quality_scores"])
            stats["success_rate"] = stats["success_count"] / stats["count"]
            stats["quality_pass_rate"] = stats["high_quality_count"] / stats["count"]
        
        return strategy_stats
    
    def _generate_recommendations(self, assessments: List[Dict[str, Any]], diversity_metrics: Dict[str, Any]) -> List[str]:
        """Generate recommendations for improving dataset quality"""
        recommendations = []
        
        # Quality recommendations
        quality_scores = [a["quality_score"] for a in assessments]
        avg_quality = sum(quality_scores) / len(quality_scores)
        
        if avg_quality < 0.6:
            recommendations.append("Overall quality is low. Consider adjusting generation parameters or filtering criteria.")
        
        # Success rate recommendations
        success_rate = sum(1 for a in assessments if a["success"]) / len(assessments)
        if success_rate < 0.5:
            recommendations.append("Low success rate. Consider reviewing task difficulty or agent capabilities.")
        
        # Diversity recommendations
        if diversity_metrics.get("content_diversity", {}).get("diversity_ratio", 0) < 0.8:
            recommendations.append("Low content diversity. Consider increasing temperature range or task variety.")
        
        # Strategy balance recommendations
        strategy_counts = {}
        for assessment in assessments:
            key = f"{assessment['agent_strategy']}_{assessment['user_strategy']}"
            strategy_counts[key] = strategy_counts.get(key, 0) + 1
        
        if len(strategy_counts) > 1:
            max_count = max(strategy_counts.values())
            min_count = min(strategy_counts.values())
            if max_count / min_count > 3:
                recommendations.append("Unbalanced strategy distribution. Consider equalizing conversation counts per strategy.")
        
        if not recommendations:
            recommendations.append("Dataset quality looks good! Consider gradual scaling or fine-tuning generation parameters.")
        
        return recommendations


def generate_quality_report(dataset: SFTDataset, output_path: str):
    """Generate a comprehensive quality report for an SFT dataset"""
    assessor = SFTQualityAssessor()
    assessment = assessor.assess_dataset(dataset)
    
    # Create formatted report
    report_lines = []
    report_lines.append("SFT Dataset Quality Report")
    report_lines.append("=" * 50)
    
    # Dataset summary
    summary = assessment["dataset_summary"]
    report_lines.append(f"\nDataset Summary:")
    report_lines.append(f"  Total conversations: {summary['total_conversations']}")
    report_lines.append(f"  High quality conversations: {summary['high_quality_conversations']}")
    report_lines.append(f"  Quality pass rate: {summary['quality_pass_rate']:.2%}")
    report_lines.append(f"  Average quality score: {summary['average_quality_score']:.3f}")
    
    # Diversity metrics
    if "diversity_metrics" in assessment:
        diversity = assessment["diversity_metrics"]
        report_lines.append(f"\nDiversity Metrics:")
        
        if "strategy_diversity" in diversity:
            strat_div = diversity["strategy_diversity"]
            report_lines.append(f"  Agent strategies: {strat_div['agent_strategies']}")
            report_lines.append(f"  User strategies: {strat_div['user_strategies']}")
            report_lines.append(f"  Domains: {strat_div['domains']}")
        
        if "content_diversity" in diversity:
            content_div = diversity["content_diversity"]
            report_lines.append(f"  Content diversity ratio: {content_div['diversity_ratio']:.2%}")
    
    # Recommendations
    if "recommendations" in assessment:
        report_lines.append(f"\nRecommendations:")
        for i, rec in enumerate(assessment["recommendations"], 1):
            report_lines.append(f"  {i}. {rec}")
    
    # Write report
    with open(output_path, 'w') as f:
        f.write('\n'.join(report_lines))
    
    return assessment