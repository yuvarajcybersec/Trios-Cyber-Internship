# Day 01 — Kali Linux & Network Setup

**Organization:** Trios Cyber  
**Internship:** Cybersecurity Internship  
**Task:** Kali Linux & Network Setup  
**Day:** 01  
**Status:** Completed  
**Environment:** Kali Linux Virtual Machine

---

## Objective

The objective of this task was to configure and verify a Kali Linux laboratory environment and perform basic system and network enumeration.

The task required identifying the system hostname, current user, network interfaces, attacker IP address, default gateway, connectivity status, and listening services.

---

## Activities Performed

The following system and network commands were executed:

```bash
hostname
whoami
ip a
ifconfig
ip route
ping -c 4 10.0.2.2
ping -c 4 8.8.8.8
sudo ss -tulnp
