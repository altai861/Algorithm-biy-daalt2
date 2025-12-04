package org.example;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.*;

public class TextJustifierTest {

    @Test
    void testGreedySingleLine() {
        List<String> words = Arrays.asList("hello", "world");
        List<String> result = TextJustifier.justifyGreedy(words, 20);

        assertEquals(1, result.size());
        assertEquals("hello world         ", result.get(0));
    }

    @Test
    void testGreedyExactFit() {
        List<String> words = Arrays.asList("abc", "de", "fgh");
        List<String> result = TextJustifier.justifyGreedy(words, 11);

        assertEquals("abc de fgh ", result.get(0));
    }

    @Test
    void testGreedyMultipleLines() {
        List<String> words = Arrays.asList("This", "is", "a", "test");
        List<String> result = TextJustifier.justifyGreedy(words, 10);

        // First line fully justified
        assertEquals("This  is a", result.get(0));

        // Last line left justified
        assertEquals("test      ", result.get(1));
    }

    @Test
    void testGreedySingleWord() {
        List<String> words = Arrays.asList("Hello");
        List<String> result = TextJustifier.justifyGreedy(words, 10);

        assertEquals("Hello     ", result.get(0));
    }

    @Test
    void testGreedySpaceDistribution() {
        List<String> words = Arrays.asList("a", "b", "c", "d");
        List<String> result = TextJustifier.justifyGreedy(words, 7);

        assertEquals("a b c d", result.get(0));
    }


    @Test
    void testDPSingleLine() {
        List<String> words = Arrays.asList("hello", "world");
        List<String> result = TextJustifier.justifyDP(words, 20);

        assertEquals(1, result.size());
        assertEquals("hello world         ", result.get(0));
    }

    @Test
    void testDPExactFit() {
        List<String> words = Arrays.asList("abc", "de", "fgh");
        List<String> result = TextJustifier.justifyDP(words, 11);

        assertEquals("abc de fgh ", result.get(0));
    }

    @Test
    void testDPMultipleLines() {
        List<String> words = Arrays.asList("This", "is", "a", "test", "example");
        List<String> result = TextJustifier.justifyDP(words, 10);

        assertTrue(result.size() >= 2);
        assertEquals(10, result.get(0).length());
        assertEquals(10, result.get(1).length());
    }

    @Test
    void testDPLastLineLeftJustified() {
        List<String> words = Arrays.asList("longword", "small", "x");
        List<String> result = TextJustifier.justifyDP(words, 15);

        assertEquals("longword  small", result.get(0));
        assertEquals("x              ", result.get(1));
    }

    @Test
    void testDPMatchesGreedyForSimpleInput() {
        List<String> words = Arrays.asList("a", "b", "c", "d");
        List<String> greedy = TextJustifier.justifyGreedy(words, 7);
        List<String> dp = TextJustifier.justifyDP(words, 7);

        assertEquals(greedy, dp);
    }

    @Test
    void testDPHandlesSingleWordLine() {
        List<String> words = Arrays.asList("Hello");
        List<String> result = TextJustifier.justifyDP(words, 10);

        assertEquals("Hello     ", result.get(0));
    }
}
