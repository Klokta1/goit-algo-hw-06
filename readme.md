### Порівняння результатів
1. **DFS**:
  - Алгоритм DFS заглиблюється в кожен вузол повністю, перш ніж переходити до наступного. Це може призвести до того, що шлях буде довшим або обійде непотрібні вузли, які спочатку трапляються в глибину.
  - У наведеному прикладі DFS може повернути шлях, наприклад, `['Alice', 'Bob', 'Eve', 'Frank', 'Grace', 'Hannah']`.

2. **BFS**:
  - Алгоритм BFS обробляє кожен рівень по черзі, тому він завжди знаходить найкоротший шлях у неорієнтованому графі, якщо він існує.

### Висновок
Різниця в отриманих шляхах для DFS і BFS обумовлена принципами роботи кожного з алгоритмів. **BFS** буде кращим вибором для знаходження найкоротшого шляху, а **DFS** підходить для завдань, де важливо дослідити всю глибину, перш ніж переходити до інших сусідів.