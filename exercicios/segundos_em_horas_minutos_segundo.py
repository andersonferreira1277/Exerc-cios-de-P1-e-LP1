s = float(input())
h = s/3600
s = s%3600
m = s/60
s = s%60
print("%.0f h %.0f m %.0f s" % (h,m,s))
