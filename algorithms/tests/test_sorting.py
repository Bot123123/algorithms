import random
import unittest
from ..sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort, shell_sort, comb_sort, cocktail_sort


class SortingAlgorithmTestCase(unittest.TestCase):
    """
    Shared code for a sorting unit test.
    """
    
    def setUp(self):
        self.input = range(10)
        random.shuffle(self.input)
        self.correct = range(10)
        print self.input
        print self.correct


class TestBubbleSort(SortingAlgorithmTestCase):
    """
    Tests Bubble sort on a small range from 0-9
    """

    def test_bubblesort(self):
        self.output = bubble_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestSelectionSort(SortingAlgorithmTestCase):
    """
    Tests Selection sort on a small range from 0-9
    """

    def test_selectionsort(self):
        self.output = selection_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestInsertionSort(SortingAlgorithmTestCase):
    """
    Tests Insertion sort on a small range from 0-9
    """

    def test_selectionsort(self):
        self.output = insertion_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestMergeSort(SortingAlgorithmTestCase):
    """
    Tests Merge sort on a small range from 0-9
    also tests merge function included in merge sort
    """

    def test_mergesort(self):
        self.output = merge_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)

    def test_merge(self):
        self.seq1 = range(0, 5)
        self.seq2 = range(5, 10)
        self.seq = merge_sort.merge(self.seq1, self.seq2)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)


class TestQuickSort(SortingAlgorithmTestCase):
    """
    Test Quick sort on a small range from 0-9
    """

    def test_quicksort(self):
        self.output = quick_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestHeapSort(SortingAlgorithmTestCase):
    """
    Test Heap sort on a small range from 0-9
    """

    def test_heapsort(self):
        self.output = heap_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestShellSort(SortingAlgorithmTestCase):
    """
    Test Shell sort on a small range from 0-9
    """

    def test_shellsort(self):
        self.output = shell_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestCombSort(SortingAlgorithmTestCase):
    """
    Test Comb sort on a small range from 0-9
    """

    def test_combsort(self):
        self.output = comb_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)

class TestCocktailSort(SortingAlgorithmTestCase):
    """
    Tests Cocktail sort on a small range from 0-9
    """

    def test_cocktailsort(self):
        self.output = cocktail_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)
