import heapq
from collections import deque

# --- TUGAS 1: SISTEM ANTRIAN DARURAT RUMAH SAKIT ---
class EmergencyQueue:
    def __init__(self):
        self.queue = []  # Inisialisasi daftar kosong sebagai heap

    def add_patient(self, name, priority):
        heapq.heappush(self.queue, (priority, name))

    def process_patient(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]  # Mengembalikan nama pasien
        return "Antrian kosong!"

    def display_queue(self):
        sorted_queue = sorted(self.queue)  # Sort berdasarkan prioritas
        print([patient[1] for patient in sorted_queue])  # Hanya menampilkan nama pasien

    def is_empty(self):
        return len(self.queue) == 0

if __name__ == "__main__":
    queue = EmergencyQueue()
    # Tambah pasien
    queue.add_patient("Andi", 2)  # Serius
    queue.add_patient("Budi", 1)  # Kritis
    queue.add_patient("Citra", 3)  # Ringan
    queue.add_patient("Dewi", 1)  # Kritis
    
    # Tampilkan antrian
    print("Antrian saat ini:")
    queue.display_queue()  # Output: ['Budi', 'Dewi', 'Andi', 'Citra']
    
    # Proses pasien
    print("Pasien diproses:", queue.process_patient())  # Output: Budi
    
    # Tampilkan antrian setelah pemrosesan
    print("Antrian setelah pemrosesan:")
    queue.display_queue()  # Output: ['Dewi', 'Andi', 'Citra']

# --- TUGAS 2: MANAJEMEN TUGAS DENGAN DEQUE ---
class TaskManager:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self):
        if not self.is_empty():
            return self.tasks.popleft()
        return "Tidak ada tugas dalam antrian!"

    def add_urgent_task(self, task):
        self.tasks.appendleft(task)

    def display_tasks(self):
        print(list(self.tasks))

    def is_empty(self):
        return len(self.tasks) == 0

if __name__ == "__main__":
    tasks = TaskManager()
    # Tambah tugas
    tasks.add_task("Kerjakan laporan")
    tasks.add_task("Meeting dengan tim")
    tasks.add_urgent_task("Bug fix urgent")  # Tugas ini masuk ke depan antrian
    
    # Tampilkan antrian tugas
    print("Daftar Tugas:")
    tasks.display_tasks()  # Output: ['Bug fix urgent', 'Kerjakan laporan', 'Meeting dengan tim']
    
    # Proses tugas
    print("Tugas dikerjakan:", tasks.remove_task())  # Output: Bug fix urgent
    
    # Tampilkan antrian setelah pemrosesan
    print("Daftar Tugas setelah pemrosesan:")
    tasks.display_tasks()  # Output: ['Kerjakan laporan', 'Meeting dengan tim']

