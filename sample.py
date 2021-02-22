import pandas as pd
import numpy as np
%matplotlib inline
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__)

import cufflinks as cf
init_notebook_mode(connected=True)
cf.go_offline()

df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)