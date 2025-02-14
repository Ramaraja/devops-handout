### **Ansible Examples**

---

### **1. Install and Configure Ansible**  

#### **Step 1: Install Ansible**  
```bash
sudo apt update && sudo apt install -y ansible  # Ubuntu/Debian
sudo yum install -y ansible  # CentOS/RHEL
```

#### **Step 2: Verify Installation**  
```bash
ansible --version
```

#### **Step 3: Configure Inventory (`/etc/ansible/hosts`)**  
```ini
[web]
192.168.1.10  ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```

Replace `192.168.1.10` with your actual server IP.  

---

### **2. Ping All Servers**

```bash
ansible all -m ping
```
**Output:**
```
192.168.1.10 | SUCCESS => {
    "ping": "pong"
}
```

---

### **3. Run a Shell Command on Remote Servers**  
**Check free disk space on all servers**  

```bash
ansible all -m shell -a "df -h"
```

---

### **4. Ansible Playbook to Install Nginx**  
**Automate Nginx installation using a playbook**  

#### **Step 1: Create `install-nginx.yaml`**  
```yaml
---
- name: Install Nginx on Ubuntu
  hosts: web
  become: yes
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install Nginx
      apt:
        name: nginx
        state: present

    - name: Start Nginx Service
      service:
        name: nginx
        state: started
        enabled: yes
```

#### **Step 2: Run the Playbook**  
```bash
ansible-playbook install-nginx.yaml
```

**Nginx will be installed and running** on the remote server.  

---

### **5. Copy Files Using Ansible**  
**Transfer a local file to the remote server**  

```yaml
---
- name: Copy a file to remote server
  hosts: web
  become: yes
  tasks:
    - name: Copy index.html
      copy:
        src: ./index.html
        dest: /var/www/html/index.html
        mode: 0644
```

**Run:**  
```bash
ansible-playbook copy-file.yaml
```

---

### **6. Create and Deploy a User with SSH Key**  
**Create a new user and add an SSH key**  

```yaml
---
- name: Create user and add SSH key
  hosts: web
  become: yes
  tasks:
    - name: Create user
      user:
        name: devops
        shell: /bin/bash
        state: present

    - name: Add SSH Key
      authorized_key:
        user: devops
        key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
```

---

### **7. Deploy Docker Using Ansible**
**Install Docker and run a container**  

```yaml
---
- name: Install Docker and run a container
  hosts: web
  become: yes
  tasks:
    - name: Install Docker
      apt:
        name: docker.io
        state: present

    - name: Start Docker service
      service:
        name: docker
        state: started
        enabled: yes

    - name: Run Nginx Container
      docker_container:
        name: nginx
        image: nginx
        state: started
        ports:
          - "80:80"
```

**Run:**  
```bash
ansible-playbook install-docker.yaml
```

**Nginx will run inside a Docker container**.

---

### **8. Ansible Roles Example**
**Organize playbooks using roles**  

#### **Step 1: Create a Role**
```bash
ansible-galaxy init roles/nginx
```

#### **Step 2: Edit `roles/nginx/tasks/main.yaml`**
```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
```

#### **Step 3: Create `nginx-playbook.yaml`**
```yaml
---
- name: Install Nginx using a role
  hosts: web
  become: yes
  roles:
    - nginx
```

#### **Step 4: Run the Playbook**
```bash
ansible-playbook nginx-playbook.yaml
```

---

### **9. Ansible + Terraform Example**
**Use Terraform to provision a server, then configure it using Ansible.**  

#### **Step 1: Create Terraform File (`main.tf`)**
```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "my-key"

  provisioner "remote-exec" {
    inline = ["sudo apt update && sudo apt install -y ansible"]
  }
}
```

#### **Step 2: Run Terraform**
```bash
terraform apply -auto-approve
```

**Terraform launches the instance, then installs Ansible**.

---
