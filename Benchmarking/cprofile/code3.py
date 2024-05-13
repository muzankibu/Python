# importing library
import cProfile
import pstats
import io
from pstats import SortKey

# Creating profile object
ob = cProfile.Profile()
ob.enable()

# As you increase the power time will increase
# as per your machine efficiency.
num = 18**200000

ob.disable()
sec = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(ob, stream=sec).sort_stats(sortby)
ps.print_stats()

print(sec.getvalue())
