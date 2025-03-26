import heapq

# --- TUGAS 1: SISTEM ANTRIAN DARURAT RUMAH SAKIT ---
class EmergencyQueue:
    def __init__(self):
        self.queue = [] #Inisialisasi dafatr kosong sebagai heap

    def add_patient(self, name, priority):
        heapq.heappush(self.queue, (priority, name))

    def prosess_patient(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1] # Mengembalikan nama pas:
        return "Antrian kosong!"
    
    def display_queue(self):
        sorted_queue = sorted(self.queue) # Sort berdasrkan proritas
        print([patient[1] for patient in sorted_queue]) 

    def is_empty(self):
        return len(self.queue) == 0
if __name__ == "__main__":
    queue = EmergencyQueue()
    # Tambah pasien
    queue.add_patient("Andi", 2) # Serius
    queue.add_patient("budi", 1) # Kritis
    queue.add_patient("Citra", 3) # Ringan
    queue.add_patient("Dewi", 1) #Kritis

    # Tampilkan antrian
    print("Antrian saat ini:")
    queue.display_queue() # Output: ['Budi', 'Dewi', 'Andi', 'Citra']

    #proses pasien
    print("Pasien diproses:", queue.prosess_patient()) # Output: Budi

    # Tampilkan antrian setelah pemrosesan
    print("Antrian setelah pemrosesan:")
    queue.display_queue() # Output: ['Dewi', 'Andi', 'Citra']