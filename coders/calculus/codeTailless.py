int fatorialSemCauda(int n) {
  if (n == 0) {
    return 1;
  } else {
    return n * fatorialSemCauda(n - 1);
  }
}
