import unittest
from WorkerDb import WorkerDB
from ClassWorker import Worker

class TestWorkerDb(unittest.TestCase):
    def test_add_worker(self):
        worker_db = WorkerDB()
        worker_db.add_worker(Worker("beb", "bebbs", "IT", 20000))
        self.assertEqual(len(worker_db.workers), 1)
        
    def test_add_worker_by_input(self):
        worker_db = WorkerDB()
        worker_db.add_worker_by_input()
        self.assertEqual(len(worker_db.workers), 1)
        
    def test_delete_by_id(self):
        worker_db = WorkerDB()
        worker_db.add_worker(Worker("beb", "bebbs", "IT", 20000))
        worker_db.add_worker(Worker("bebaaa", "bebbsaa", "ITsh", 3000))
        worker_db.delete_by_id(1)
        self.assertEqual(len(worker_db.workers), 1)
        worker_db.delete_by_id(0)
        self.assertEqual(len(worker_db.workers), 0)
        
    def test_edit_by_id(self):
        worker_db = WorkerDB()
        worker_db.add_worker(Worker("beb", "bebbs", "IT", 20000))
        worker_db.edit_by_id(0, "name", "bebaaa")
        self.assertEqual(worker_db.workers[0].name, "bebaaa")
        worker_db.edit_by_id(0, "second name", "bebbsaa")
        self.assertEqual(worker_db.workers[0].secname, "bebbsaa")
        worker_db.edit_by_id(0, "departament", "ITsh")
        self.assertEqual(worker_db.workers[0].departament, "ITsh")
        worker_db.edit_by_id(0, "salary", 3000)
        self.assertEqual(worker_db.workers[0].salary, 3000)
        
    def test_sort(self):
        worker_db = WorkerDB()
        worker_db.add_worker(Worker("bebr", "bebbsr", "IT", 20000))
        worker_db.add_worker(Worker("bebaaa", "bebbsaa", "ITsh", 3000))
        worker_db.sort("name")
        self.assertEqual(worker_db.workers[0].name, "bebaaa")
        worker_db.sort("secname")
        self.assertEqual(worker_db.workers[0].secname, "bebbsaa")
        worker_db.sort("departament")
        self.assertEqual(worker_db.workers[0].departament, "IT")
        worker_db.sort("salary")
        self.assertEqual(worker_db.workers[0].salary, 3000)
        
    def test_search(self):
        worker_db = WorkerDB()
        worker_db.add_worker(Worker("bebr", "bebbsr", "IT", 20000))
        worker_db.add_worker(Worker("bebaaa", "bebbsaa", "ITsh", 3000))
        res = worker_db.search("name", "bebr")
        self.assertEqual(res[0].name, "bebr")
        res = worker_db.search("secname", "bebbsr")
        self.assertEqual(res[0].secname, "bebbsr")
        res = worker_db.search("departament", "skjdas")
        self.assertEqual(res, [])
        
if __name__ == "__main__":
    unittest.main()