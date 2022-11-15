# PSYCH 403 - Assignment 7 exercises: MPacificar

## Wait exercises
Fill in the following pseudocode with the real code you have learned so far using "core.wait" (and run it to make sure it works):
```

```

## Clock exercises
1. Create a "wait_timer" to find out exactly how long core.wait(2) presents each image. Make sure this is not counting the time of the whole trial, but only the duration of each image. How precise is core.wait?
```

```
2. Create a "clock_wait_timer" to find out exactly how long each image is presented when you use a clock + while loops. How precise is this?
```

```
3. Create a "countdown_timer" to find out exactly how long each image is presented when you use a CountdownTimer + while loops. How precise is this?
```

```
4. Edit your main experiment script so that the trials loop according to a clock timer. Also create and implement a block_timer and a trial_timer.
```

```

## Frame-based timing exercises
1. Adjust your experiment so that it follows frame-based timing rather than clock timing (comment out the clock-based timing code in case you want to use it again) using for loops and if statements.
```

```
2. Add a "dropped frame" detector to your script to find out whether your experiment is dropping frames. How many total frames are dropped in the experiment? If 20 or fewer frames are dropped in the whole experiment (1 frame per trial), keep frame-based timing in your experiment. Otherwise, switch back to the CountdownTimer.
```

```
