# API

### Manually save a new state:

```bash
cd manual_save_state
python retro_interactive.py --state "Champion.Start.RyuVsRyu.2Player" # press 'SPACE' during game to save state
python move_state.py # specify the state file to move
```

### Train a new AI against baseline:

```bash
python train.py
```

### Test one side human, one side AI:

```bash
python play_with_ai.py
```

### Test two-side AI:

```bash
python test_ai_vs_ai.py
```



References:

https://github.com/linyiLYi/street-fighter-ai

https://github.com/tonyxu99/String_fighter_AI

