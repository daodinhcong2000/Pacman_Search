# Pacman-AI

1. DFS
   -Sử dụng 1 Stack để lưu trạng thái và đường đi đến trạng thái đó + 1 mảng để lưu các toạ độ đã thăm + 1 mảng để lưu các đường đã đi để tới được trạng thái đích
   -Push trạng thái ban đầu vào stack và đánh dấu là đã thăm
   -Khi stack còn phần tử ta sẽ chạy vòng lặp:
   +Gán trạng thái đang duyệt = pop Stack
   +Nếu trạng thái đang duyệt là trạng thái kết thúc thì dừng thuật toán
   +Push tất cả các trạng thái (trừ các trạng thái đã duyệt) có thể tới được từ trạng thái đang duyệt vào Stack

2. BFS
   -Sử dụng 1 Queue để lưu trạng thái và đường đi đến trạng thái đó + 1 mảng để lưu các đoạ độ đã thăm + 1 mảng để lưu các đường đã đi để tới trạng thái đích
   -Push trạng thái ban đầu vào queue và đánh dấu là đã thăm
   -Khi queue còn phần tử ta sẽ chạy vòng lặp:
   +Gán trạng thái đang duyệt = pop Queue
   +Nếu trạng thái đang duyệt là trạng thái kết thúc thì dừng thuật toán
   +Push tất cả các trạng thái (trừ các trạng thái đã duyệt) có thể tới được từ trạng thái đang duyệt vào Queue

3. UCS
   -Sử dụng 1 Priority Queue (với priority là giá của nước đi) để lưu trạng thái và đường đi đến trạng thái đó + 1 mảng để lưu các đoạ độ đã thăm + 1 mảng để lưu các đường đã đi để tới trạng thái đích
   -Push trạng thái ban đầu vào queue và đánh dấu là đã thăm
   -Khi queue còn phần tử ta sẽ chạy vòng lặp:
   +Gán trạng thái đang duyệt = pop Queue
   +Nếu trạng thái đang duyệt là trạng thái kết thúc thì dừng thuật toán
   +Push tất cả các trạng thái (trừ các trạng thái đã duyệt) có thể tới được từ trạng thái đang duyệt vào Queue

4. A\*

- Tương đương UCS với priority = g(n) + h(n)
  +g(n) = giá của nước đi
  +h(n) là khoảng cách manhattan

5. Finding All the Corners

- khởi tạo trạng thái ban đầu là [0,0,0,0] tức là cả 4 góc chưa được thăm.

  6.Corners Problem: Heuristic

- Trả về khoảng cách ngắn nhất trong các khoảng cách từ vị trí hiện tại đến 4 góc.
