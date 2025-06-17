## error
```
task02.py:37: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
  plt.show()
```

### fix

https://stackoverflow.com/questions/77507580/userwarning-figurecanvasagg-is-non-interactive-and-thus-cannot-be-shown-plt-sh/78344937#78344937

```
sudo apt-get install python3-tk
```