# Trios Cyber Internship — Day 01 Technical Report

## Kali Linux & Network Setup

**Organization:** Trios Cyber  
**Internship:** Cybersecurity Internship  
**Task:** Kali Linux & Network Setup  
**Day:** 01  
**Date:** 01 September 2026  
**Environment:** Kali Linux Virtual Machine  
**Virtualization Platform:** Oracle VirtualBox  
**Status:** Completed

---

## 1. Executive Summary

The Day 01 task focused on establishing and validating a Kali Linux virtual laboratory environment and performing basic system and network enumeration.

The assessment covered system identification, network interface enumeration, IP address identification, routing analysis, connectivity verification, and listening-service enumeration.

Screenshots and raw command outputs were preserved as supporting evidence.

---

## 2. Objectives

The objectives of this task were to:

1. Verify the Kali Linux hostname.
2. Identify the current user.
3. Enumerate available network interfaces.
4. Identify the lab/attacker IP address.
5. Identify the default gateway.
6. Verify local network connectivity.
7. Verify external network connectivity.
8. Enumerate listening TCP/UDP services.
9. Document the results using screenshots and command logs.

---

## 3. Lab Environment

| Parameter | Value |
|---|---|
| Operating System | Kali Linux |
| Environment | Virtual Machine |
| Virtualization | Oracle VirtualBox |
| Primary Interface | `eth0` |
| Network Configuration | VirtualBox NAT |
| Lab/Attacker IPv4 | `10.0.2.15/24` |

---

## 4. System Identification

### 4.1 Hostname

Command:

```bash
hostname

