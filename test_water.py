from water import daily_demand

def test_daily_demand_values():
  assert daily_demand(5000,100) == 500000

def something_true():
  assert 1 == 1
  assert daily_demand(5000,0) == 0
