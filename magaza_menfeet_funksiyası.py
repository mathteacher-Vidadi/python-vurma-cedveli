def menfeet_hesabla(alis, satis, say):
    menfeet = (satis - alis) * say
    if menfeet > 0:
      print("Mənfəət:", menfeet, "manat")
      print("Mağaza məmfəət edib.")
    else:
      print("zərər:", abs(menfeet), "manat")
      print("Mağaza zərər edib.")
menfeet_hesabla(5.00, 7.50, 20)
menfeet_hesabla(7.50, 5.00, 20)   
