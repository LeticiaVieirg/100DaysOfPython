int factorial_tailless(int n) {
  if (n == 0) {
    return 1;
  } else {
    return n * factorial_tailless(n - 1);
  }
}
