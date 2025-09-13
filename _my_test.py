from skyrl_train.models import Actor
import torch

print('Creating LoRA Actor...')
actor = Actor(
    'Qwen/Qwen2.5-0.5B-Instruct',
    lora_rank=8, 
    lora_alpha=16,
    target_modules=['q_proj', 'v_proj'],
    device_map='cpu'
)

print('\nFirst 15 parameter names:')
for i, (name, param) in enumerate(actor.model.named_parameters()):
    print(f'  {name}')
    if i >= 14:
        break

print('\nParameters starting with base_model:')
base_model_params = [name for name, _ in actor.model.named_parameters() if name.startswith('base_model.')]
print(f'Found {len(base_model_params)} base_model parameters')
for name in base_model_params[:5]:
    print(f'  {name}')

print('\nParameters NOT starting with base_model:')
non_base_model_params = [name for name, _ in actor.model.named_parameters() if not name.startswith('base_model.')]
print(f'Found {len(non_base_model_params)} non-base_model parameters')  
for name in non_base_model_params[:5]:
    print(f'  {name}')