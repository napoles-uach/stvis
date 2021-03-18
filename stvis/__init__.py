import streamlit.components.v1 as components
def pv_static(fig,name='graph'):
  h1=fig.height
  h1=int(h1.replace('px',''))
  w1=fig.width
  w1=int(w1.replace('px',''))
  fig.show(name+'.html')
  return components.html(
    fig.html,height=h1+30, width=w1+30
       )