import sortRunner
import selectionSort

__Author__ = 'Tarik'

Ints = sortRunner.getIntArray()
Strings = sortRunner.getStringArray()

print "SelectedSort"
sortRunner.sort(selectionSort.sort, Ints)
print "\n"
sortRunner.sort(selectionSort.sort, Strings)
print "\n"*2