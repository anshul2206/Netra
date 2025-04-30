# Netra 🔍

Netra is a lightweight network scanner written in Python that uses ARP requests to discover devices in a local network. It provides a simple command-line interface for identifying IP and MAC addresses of devices connected to the network.

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/anshul2206/netra.git
cd netra
```

Install dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Make the script executable (optional):

```bash
chmod +x NetworkScanner.py
```

---

## 🧰 Requirements

- Python 3.x
- `scapy` library
- Root/sudo privileges (required to send ARP requests)

---

## ▶️ Usage

```bash
sudo python3 NetworkScanner.py -i [IP_ADDRESS or IP_RANGE]
```

### 📌 Examples

Scan a specific IP:

```bash
sudo python3 NetworkScanner.py -i 192.168.1.1
```

Scan an IP range:

```bash
sudo python3 NetworkScanner.py -i 192.168.1.1/24
```

---

## 💡 Sample Output

```text
IP              MAC Address
-----------------------------------------
192.168.1.1     aa:bb:cc:dd:ee:ff
192.168.1.102   11:22:33:44:55:66
```

---

## ⚠️ Notes

- Only works on local networks.
- Must be run with administrator privileges.
- Ensure your firewall allows ARP requests.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

Developed by **ANSHUL PURI**  
GitHub: [@anshul2206](https://github.com/anshul2206)

