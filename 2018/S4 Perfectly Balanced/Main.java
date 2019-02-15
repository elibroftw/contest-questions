/**
 * 2018 S4 Perfectly Balanced
 * Still not fast enough, must be an algorithmic error
 */
import java.io.*;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class Main {
    static Map<Long, Long> cache = new ConcurrentHashMap<>();
  public static void main(String [] args) throws Exception {
    Scanner in = new Scanner(System.in);
    long N = in.nextLong();
    System.out.println(PerfectlyBalanced(N));
  }
  public static long PerfectlyBalanced(long w) {
      if (w == 2 || w == 1) return 1;
      
      else if (!cache.containsKey(w)) {
          long output = 0;
          for(long i = 2; i < w + 1; i++) {
              output += PerfectlyBalanced(w / i);
          }
          cache.put(w, output);
      }
      return cache.get(w);
  }
}
