
---

## 👁️ Vision Pipeline

- Region-of-interest cropping
- Grayscale conversion
- Frame stacking (temporal awareness)
- Normalization for CNN input

This enables the agent to infer motion, position, and objectives purely from pixels.

---

## 🎯 Action Space

The agent maps discrete actions to keyboard inputs such as:
- Move left / right
- Jump
- Attack
- Idle

This abstraction allows learning meaningful behavior without hardcoding logic.

---

## 🏆 Learning Algorithm

- **Algorithm:** Proximal Policy Optimization (PPO)
- **Policy:** CNN-based policy
- **Training:** On-policy, continuous rollout
- **Reward Shaping:** Encourages goal-directed movement and task completion

---
⚠️ Disclaimer

This project is for educational and research purposes only.
Blasphemous 2 is the property of its respective owners.

🙌 What This Project Demonstrates

Real-world reinforcement learning constraints

Vision-based decision making

PPO training stability on CPU

End-to-end RL system design

Game AI without engine access
