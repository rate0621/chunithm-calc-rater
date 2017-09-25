import bottle as btl

def session_set(k,v):
  '''setting the value of k as v in the session'''
  s = btl.request.environ['beaker.session']
  s[k]=v
  s.save()


def session_get(k, delete=False):
  '''getting value of k from the session'''
  s = btl.request.environ['beaker.session']
  v=s[k] if k in s else ''
  if delete and k in s:
      del s[k]
  return v
