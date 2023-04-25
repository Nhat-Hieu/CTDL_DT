# Định nghĩa một nút trong danh sách liên kết đơn
class Node:
    # hàm khởi tạo của lớp nút
    def __init__(self, data):
        # thuộc tính data để lưu trữ dữ liệu của nút
        self.data = data
        # lưu trữ địa chỉ của nút tiếp theo trong danh sách liên kết
        # nút tiếp theo không xác định nên thuộc tính self.next được gán bằng None
        self.next = None
# Định nghĩa một danh sách liên kết đơn
class LinkedList:
    def __init__(self):
        # lưu trữ địa chỉ của nút đầu tiên trong danh sách
        # không có nút nào được chèn vào danh sách nên giá trị của thuộc tính self.head được gán bằng None
        self.head = None

##  Thêm một nút mới chứa dữ liệu data vào đầu danh sách
    def add_to_head(self, data):
        # tạo một nút mới
        new_node = Node(data)
        # liên kết nút mới với nút hiện tại đầu tiên của danh sách liên kết
        new_node.next = self.head
        # cập nhật địa chỉ của nút đầu tiên của danh sách liên kết
        self.head = new_node

## Thêm một nút mới chứa dữ liệu data vào cuối danh sách
    def add_to_tail(self, data):
        # tạo một nút mới
        new_node = Node(data)
        # kiểm tra xem danh sách liên kết có rỗng không
        # bằng cách kiểm tra xem giá trị của self.head có phải là None hay không
        if self.head is None:
            # Nếu danh sách rỗng, nút mới sẽ trở thành nút đầu tiên của danh sách bằng cách gán giá trị self.head bằng nút mới
            self.head = new_node
        else:
            # Nếu không, một biến tạm thời current được sử dụng để lặp lại danh sách
            # cho đến khi tìm thấy nút cuối cùng (current.next là None), sau đó nút mới được thêm vào đằng sau nút cuối cùng
            current = self.head
            # kiểm tra xem nút tiếp theo của danh sách liên kết có tồn tại hay không
            # Nếu tồn tại, thì vòng lặp sẽ tiếp tục chạy
            # Nếu là None, thì vòng lặp sẽ kết thúc và đã đến cuối danh sách
            while current.next is not None:
                current = current.next
            current.next = new_node

## Xóa nút chứa dữ liệu data khỏi danh sách
    def remove(self, data):
        # Nếu danh sách liên kết đang rỗng (self.head là None), thì không có gì để xóa, trả về None
        if self.head is None:
            return
        # Nếu dữ liệu muốn xóa nằm ở đầu danh sách (self.head.data == data)
        # cập nhật head của danh sách để trỏ tới nút tiếp theo và trả về None
        if self.head.data == data:
            self.head = self.head.next
            return
        # Tạo một biến tạm thời current để lặp lại danh sách, bắt đầu từ đầu danh sách (self.head)
        current = self.head
        # Vòng lặp while sẽ chạy cho đến khi current trỏ tới nút cuối cùng trong danh sách
        while current.next is not None:
            #  Kiểm tra xem nút tiếp theo của current có chứa dữ liệu muốn xóa hay không.
            if current.next.data == data:
                # Nếu có, cập nhật nút tiếp theo của current để trỏ tới nút tiếp theo của nó (current.next.next)
                # để loại bỏ nút chứa dữ liệu muốn xóa và trả về None
                current.next = current.next.next
                return
            # Nếu không tìm thấy nút chứa dữ liệu muốn xóa, cập nhật current để trỏ tới nút tiếp theo trong danh sách
            # và tiếp tục lặp lại vòng lặp while
            current = current.next

## Tìm kiếm nút chứa dữ liệu data trong danh sách
    def search(self, data):
        # gán biến current bằng nút đầu tiên của danh sách liên kết, đây là điểm bắt đầu cho quá trình tìm kiếm
        current = self.head
        # Vòng lặp sẽ tiếp tục cho đến khi current không còn là None
        # Vòng lặp sẽ lặp lại qua tất cả các nút trong danh sách liên kết
        while current is not None:
            # kiểm tra xem giá trị của data có bằng với giá trị data của nút hiện tại hay không
            if current.data == data:
                # Nếu có, trả về True, cho biết rằng giá trị được tìm thấy
                return True
            # gán current bằng nút kế tiếp trong danh sách liên kết, để vòng lặp có thể tiếp tục kiểm tra các nút còn lại
            current = current.next
            # Nếu vòng lặp kết thúc mà không tìm thấy nút với giá trị data mong muốn, trả về False
            # cho biết rằng giá trị không được tìm thấy
        return False

llist = LinkedList()

# Yêu cầu người dùng nhập vào số lượng phần tử cần thêm vào danh sách
n = int(input("Nhập số lượng phần tử cần thêm vào danh sách: "))

# Yêu cầu người dùng nhập vào từng phần tử và thêm vào danh sách theo mong muốn
for i in range(n):
    value = input("Nhập giá trị cho phần tử thứ " + str(i+1) + ": ")
    position = input("Bạn muốn thêm phần tử vào đầu (D) hay cuối (C) danh sách? ")
    if position.upper() == "D":
        llist.add_to_head(value)
    else:
        llist.add_to_tail(value)

# Xóa phần tử khỏi danh sách
llist.remove(input("Xóa phần tử: "))

# In kết quả
print("Kết quả sau khi thực hiện thao tác được trả về như sau:")
current = llist.head
while current is not None:
    print(current.data)
    current = current.next

# Kiểm tra phần tử có tồn tại trong danh sách hay không
if llist.search(input("Nhập phần tử cần kiểm tra: ")):
    print("Phần tử có tồn tại trong danh sách")
else:
    print("Phần tử không tồn tại trong danh sách")
