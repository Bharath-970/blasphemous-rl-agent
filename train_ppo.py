from stable_baselines3 import PPO
from blasphemous_env import BlasphemousEnv

env = BlasphemousEnv()

model = PPO(
    "CnnPolicy",
    env,
    verbose=1,
    n_steps=128,
    batch_size=64,
    learning_rate=3e-4,
    gamma=0.99
)

model.learn(total_timesteps=50_000)

model.save("models/ppo_blasphemous")

print("Training complete")
