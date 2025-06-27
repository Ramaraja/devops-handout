
## Prerequisites

* Ansible installed:

  ```bash
  sudo apt install ansible  # Debian/Ubuntu  
  sudo yum install ansible  # RHEL/CentOS  
  brew install ansible      # macOS
  ```

---

## Beginner Exercises (01–10)

### 01. **Ping Test**

```bash
ansible-playbook -i 01_ping_inventory/inventory 01_ping_inventory/ping.yml
```

### 02. **Create File**

```bash
ansible-playbook -i 02_create_file/inventory 02_create_file/create_file.yml
```

### 03. **Install Package**

```bash
ansible-playbook -i 03_install_package/inventory 03_install_package/install_httpd.yml
```

### 04. **Template File**

```bash
ansible-playbook -i 04_template/inventory 04_template/hello_template.yml
```

### 05. **Add User**

```bash
ansible-playbook -i 05_user_add/inventory 05_user_add/add_user.yml
```

### 06. **Copy File**

```bash
ansible-playbook -i 06_copy_file/inventory 06_copy_file/copy_file.yml
```

### 07. **Manage httpd Service**

```bash
ansible-playbook -i 07_service/inventory 07_service/httpd_service.yml
```

### 08. **Create Multiple Users**

```bash
ansible-playbook -i 08_loop_users/inventory 08_loop_users/multiple_users.yml
```

### 09. **Conditional Execution**

```bash
ansible-playbook -i 09_when_condition/inventory 09_when_condition/conditional_task.yml
```

### 10. **Display System Facts**

```bash
ansible-playbook -i 10_fact_gather/inventory 10_fact_gather/fact_demo.yml
```


### 11. **Use Handlers**

```bash
ansible-playbook -i 01_handlers/inventory 01_handlers/handlers.yml
```

### 12. **Role-Based Setup**

```bash
cd 02_roles_site_structure
ansible-playbook -i inventory site.yml
cd ..
```

### 13. **Use Tags**

Run all:

```bash
ansible-playbook -i 03_tags/inventory 03_tags/tags_demo.yml
```

Run only tag `install`:

```bash
ansible-playbook -i 03_tags/inventory 03_tags/tags_demo.yml --tags install
```

### 14. **Multiple Handlers Notification**

```bash
ansible-playbook -i 04_notify_multiple_handlers/inventory 04_notify_multiple_handlers/notify_multi.yml
```

### 15. **Templating with Facts**

```bash
ansible-playbook -i 05_template_facts/inventory 05_template_facts/templated_facts.yml
```

---

## Notes

* Use `--check` for dry-run mode.
* Use `-v` or `-vvv` for verbose output.
* For roles, Ansible automatically picks `tasks/main.yml` from the role.

---
