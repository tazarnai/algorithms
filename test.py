import sortRunner
import selectionSort
import insertSort
import shellSort
import quickSort
import bubbleSort
import compSort
import heapSort

__Author__ = 'Tarik'

print "SelectedSort"
sortRunner.sort(selectionSort.sort, sortRunner.getIntArray())
print "\n"
sortRunner.sort(selectionSort.sort, sortRunner.getStringArray())
print "\n"*2

print "InsertSort"
sortRunner.sort(insertSort.sort, sortRunner.getIntArray())
print "\n"
sortRunner.sort(insertSort.sort, sortRunner.getStringArray())
print "\n"*2

print "ShellSort"
sortRunner.sort(shellSort.sort, sortRunner.getIntArray())
print "\n"
sortRunner.sort(shellSort.sort, sortRunner.getStringArray())
print "\n"*2

print "QuickSort"
sortRunner.sort(quickSort.sort, sortRunner.getIntArray())
print "\n"
sortRunner.sort(quickSort.sort, sortRunner.getStringArray())
print "\n"*2

print "BubbleSort"
sortRunner.sort(bubbleSort.sort, sortRunner.getIntArray())
print "\n"
sortRunner.sort(bubbleSort.sort, sortRunner.getStringArray())
print "\n"*2

print "CompSort"
sortRunner.sort(compSort.sort, sortRunner.getIntArray())
print "\n"
sortRunner.sort(compSort.sort, sortRunner.getStringArray())
print "\n"*2

print "HeapSort"
sortRunner.sort(heapSort.sort, sortRunner.getIntArray())
print "\n"
sortRunner.sort(heapSort.sort, sortRunner.getStringArray())
print "\n"*2

