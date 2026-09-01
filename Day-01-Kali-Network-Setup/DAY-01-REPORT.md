# Trios Cyber Internship — Day 01 Technical Report

## Kali Linux & Network Setup

**Organization:** Trios Cyber  
**Internship:** Cybersecurity Internship  
**Task:** Kali Linux & Network Setup  
**Day:** 01  
**Date:** 01 September 2026  
**Environment:** Kali Linux Virtual Machine  
**Virtualization Platform:** Oracle VirtualBox  
**Network Mode:** NAT  
**Status:** Completed

---

## 1. Executive Summary

The Day 01 task focused on establishing and validating a Kali Linux virtual laboratory environment and performing basic system and network enumeration.

The assessment covered system identification, network interface enumeration, IP address identification, routing analysis, connectivity verification, and listening-service enumeration.

All required commands were executed in the Kali Linux lab environment. Command outputs were preserved as raw log files, and screenshots were captured as evidence.

---

## 2. Objectives

The objectives of this task were to:

1. Verify the Kali Linux hostname.
2. Identify the current user.
3. Enumerate available network interfaces.
4. Identify the lab/attacker IP address.
5. Identify the default gateway.
6. Inspect the routing table.
7. Verify local network connectivity.
8. Verify external network connectivity.
9. Enumerate listening TCP/UDP services.
10. Document the results using screenshots and command logs.

---

## 3. Lab Environment

| Parameter | Value |
|---|---|
| Operating System | Kali Linux |
| Environment | Virtual Machine |
| Virtualization | Oracle VirtualBox |
| Network Mode | NAT |
| Primary Interface | `eth0` |
| Lab/Attacker IPv4 | `10.0.2.15/24` |
| Default Gateway | `10.0.2.2` |
| Loopback Address | `127.0.0.1` |

---

## 4. System Identification

### 4.1 Hostname

**Command:**

```bash
hostname
```

**Result:**

```text
kali
```

The hostname of the Kali Linux system was confirmed as `kali`.

**Evidence:** `screenshots/01-hostname.png`

---

### 4.2 Current User

**Command:**

```bash
whoami
```

**Result:**

```text
yuvaraj
```

The current logged-in user was confirmed as `yuvaraj`.

**Evidence:** `screenshots/02-whoami.png`

---

## 5. Network Interface Enumeration

### 5.1 IP Address and Interface Configuration

**Command:**

```bash
ip a
```

The primary network interface identified was:

```text
eth0
```

The assigned IPv4 address was:

```text
10.0.2.15/24
```

The loopback interface was:

```text
lo
127.0.0.1/8
```

The `eth0` interface was operational and configured with the `10.0.2.0/24` network.

**Evidence:** `screenshots/03-ip-a.png`

---

### 5.2 Legacy Interface Information

**Command:**

```bash
ifconfig
```

The `ifconfig` output confirmed:

```text
Interface: eth0
IPv4 Address: 10.0.2.15
Netmask: 255.255.255.0
Broadcast: 10.0.2.255
```

The interface reported no RX or TX errors during the captured observation.

**Evidence:** `screenshots/04-ifconfig.png`

---

## 6. Routing Analysis

### 6.1 Routing Table

**Command:**

```bash
ip route
```

The default route was identified as:

```text
default via 10.0.2.2 dev eth0
```

The local network route was:

```text
10.0.2.0/24 dev eth0
```

### Routing Findings

| Parameter | Value |
|---|---|
| Default Gateway | `10.0.2.2` |
| Interface | `eth0` |
| Local Network | `10.0.2.0/24` |
| Source IP | `10.0.2.15` |

The routing configuration indicates that traffic outside the local `10.0.2.0/24` network is forwarded through `10.0.2.2`.

**Evidence:** `screenshots/05-ip-route.png`

---

## 7. Connectivity Verification

### 7.1 Gateway Connectivity

The default gateway was tested using ICMP:

```bash
ping -c 4 10.0.2.2
```

**Result:**

```text
4 packets transmitted
4 packets received
0% packet loss
```

Average round-trip time:

```text
0.445 ms
```

This confirmed successful communication between the Kali VM and its configured gateway.

**Raw output:** `logs/ping-gateway.txt`

---

### 7.2 External Network Connectivity

External connectivity was tested using Google's public DNS server:

```bash
ping -c 4 8.8.8.8
```

**Result:**

```text
4 packets transmitted
4 packets received
0% packet loss
```

Average round-trip time:

```text
7.590 ms
```

This confirmed that the Kali VM had functional external network connectivity.

**Raw output:** `logs/ping-internet.txt`

**Evidence:** `screenshots/06-ping.png`

---

## 8. Listening Service Enumeration

Listening TCP/UDP services were checked using the socket listing output.

The captured result contained only the header:

```text
Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port Process
```

No listening services were reported during the observation.

This indicates that no TCP/UDP listening sockets were detected at the time of enumeration.

**Raw output:** `logs/listening-services.txt`

**Evidence:** `screenshots/07-listening-services.png`

---

## 9. Network Configuration Summary

| Item | Finding |
|---|---|
| Hostname | `kali` |
| Current User | `yuvaraj` |
| Primary Interface | `eth0` |
| Lab/Attacker IPv4 | `10.0.2.15/24` |
| Local Network | `10.0.2.0/24` |
| Default Gateway | `10.0.2.2` |
| Loopback | `127.0.0.1` |
| Gateway Connectivity | Successful |
| Gateway Packet Loss | `0%` |
| External Connectivity | Successful |
| External Packet Loss | `0%` |
| Listening Services | None reported |

---

## 10. Evidence and Documentation

The following evidence was collected during the task.

### Screenshots

| File | Evidence |
|---|---|
| `01-hostname.png` | Hostname verification |
| `02-whoami.png` | Current user verification |
| `03-ip-a.png` | IP addresses and interfaces |
| `04-ifconfig.png` | Interface configuration |
| `05-ip-route.png` | Routing table |
| `06-ping.png` | Connectivity testing |
| `07-listening-services.png` | Listening-service enumeration |

### Raw Logs

| File | Description |
|---|---|
| `day1-network-enumeration.txt` | Main enumeration output |
| `network-summary.txt` | Network configuration summary |
| `listening-services.txt` | Listening-service enumeration |
| `ping-gateway.txt` | Gateway connectivity test |
| `ping-internet.txt` | External connectivity test |

---

## 11. Commands Practiced

The following Linux networking and system-identification commands were used:

```bash
hostname
whoami
ip a
ifconfig
ip route
ping -c 4 10.0.2.2
ping -c 4 8.8.8.8
```

Listening services were also enumerated using the socket listing functionality.

These commands provided practical exposure to system identification, interface discovery, routing analysis, connectivity testing, and basic service enumeration.

---

## 12. Conclusion

The Day 01 Kali Linux and Network Setup task was completed successfully in a dedicated VirtualBox-based Kali Linux laboratory environment.

The Kali VM was identified, its network interfaces and IP configuration were enumerated, the default gateway and routing table were identified, and network connectivity was successfully verified.

The environment demonstrated:

- A functional `eth0` interface.
- Lab IP address `10.0.2.15/24`.
- Default gateway `10.0.2.2`.
- Successful gateway connectivity with `0%` packet loss.
- Successful external connectivity with `0%` packet loss.
- No listening TCP/UDP services reported during the observation.

All required evidence was organized into screenshots and raw command-output logs for reproducibility and review.

---

## 13. Repository Structure

```text
Day-01-Kali-Network-Setup/
├── README.md
├── DAY-01-REPORT.md
├── logs/
│   ├── day1-network-enumeration.txt
│   ├── listening-services.txt
│   ├── network-summary.txt
│   ├── ping-gateway.txt
│   └── ping-internet.txt
└── screenshots/
    ├── 01-hostname.png
    ├── 02-whoami.png
    ├── 03-ip-a.png
    ├── 04-ifconfig.png
    ├── 05-ip-route.png
    ├── 06-ping.png
    └── 07-listening-services.png
```

---

**Prepared for:** Trios Cyber Internship  
**Task:** Day 01 — Kali Linux & Network Setup
