# %%
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
data.plot(x="x", y="y")
plt.show()


# %%
