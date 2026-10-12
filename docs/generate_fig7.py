import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set high DPI and aesthetic styling
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'

fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
ax.set_xlim(0, 140)
ax.set_ylim(0, 80)
ax.axis('off')

# Background container (light slate gray app container)
bg_card = patches.FancyBboxPatch((2, 2), 136, 76, boxstyle="round,pad=0.8,rounding_size=1.5",
                                 facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.5)
ax.add_patch(bg_card)

# Top Navigation Bar / Worker Profile Header
header_bar = patches.FancyBboxPatch((4, 70), 132, 6.5, boxstyle="round,pad=0.4,rounding_size=0.8",
                                   facecolor='#1e293b', edgecolor='none')
ax.add_patch(header_bar)

ax.text(7, 73.2, "WORKER FIELD TERMINAL & LIVE DISPATCH INTERFACE", color='white',
        fontsize=13, fontweight='bold', va='center')

# Online Status pill
status_pill = patches.FancyBboxPatch((110, 71.5), 23, 3.5, boxstyle="round,pad=0.3,rounding_size=1.0",
                                     facecolor='#10b981', edgecolor='none')
ax.add_patch(status_pill)
ax.text(121.5, 73.2, "● LIVE & AVAILABLE", color='white', fontsize=9.5, fontweight='bold', ha='center', va='center')

# Worker Profile Sub-header card
worker_info_box = patches.FancyBboxPatch((4, 60), 132, 8.5, boxstyle="round,pad=0.4,rounding_size=0.6",
                                        facecolor='#ffffff', edgecolor='#e2e8f0', linewidth=1.2)
ax.add_patch(worker_info_box)

ax.text(7, 65.5, "K. Ramesh Babu", fontsize=14, fontweight='bold', color='#0f172a')
ax.text(7, 62.2, "Senior Certified Electrician & Household Plumber | Danavaipeta Zone, Ward 7", fontsize=9.5, color='#64748b')

# 4 Key Metrics Badges
metrics = [
    ("TODAY'S EARNINGS", "₹1,850", "#059669", 68),
    ("COMPLETED JOBS", "4 Tasks", "#2563eb", 85),
    ("BILATERAL ELO", "1,842 (Diamond)", "#7c3aed", 102),
    ("CLIENT RATING", "4.89 / 5.0 (148)", "#d97706", 121)
]

for label, val, col, x_pos in metrics:
    m_box = patches.FancyBboxPatch((x_pos, 61), 15.5, 6.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                  facecolor='#f1f5f9', edgecolor='#e2e8f0')
    ax.add_patch(m_box)
    ax.text(x_pos + 7.75, 65.5, val, fontsize=10, fontweight='bold', color=col, ha='center')
    ax.text(x_pos + 7.75, 62.5, label, fontsize=6.8, color='#64748b', ha='center', fontweight='bold')

# ----------------- LEFT PANEL: Incoming Dispatch & Recurring Contracts (Width 64) -----------------
panel_left = patches.FancyBboxPatch((4, 4), 64, 54, boxstyle="round,pad=0.5,rounding_size=0.8",
                                   facecolor='#ffffff', edgecolor='#e2e8f0', linewidth=1.2)
ax.add_patch(panel_left)

ax.text(7, 54.5, "Incoming Job Dispatches (Real-Time Push)", fontsize=11.5, fontweight='bold', color='#1e293b')
ax.text(7, 52.2, "Filtered by Geofence (Haversine r <= 3.5 km) & Skill Matching Engine", fontsize=8.2, color='#64748b')

# Dispatch Item 1: High Priority Recurring Contract
item1_box = patches.FancyBboxPatch((6, 31), 60, 19, boxstyle="round,pad=0.4,rounding_size=0.6",
                                  facecolor='#f8fafc', edgecolor='#6366f1', linewidth=1.5)
ax.add_patch(item1_box)

# Tag
rec_tag = patches.FancyBboxPatch((8, 45.8), 24, 2.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor='#e0e7ff', edgecolor='#c7d2fe')
ax.add_patch(rec_tag)
ax.text(20, 47.2, "RECURRING SUBSCRIPTION", fontsize=7.5, fontweight='bold', color='#4338ca', ha='center', va='center')

urgent_tag = patches.FancyBboxPatch((33, 45.8), 16, 2.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                   facecolor='#fef3c7', edgecolor='#fde68a')
ax.add_patch(urgent_tag)
ax.text(41, 47.2, "AI MATCH: 96.4%", fontsize=7.5, fontweight='bold', color='#b45309', ha='center', va='center')

ax.text(8, 43.5, "Daily Electrical & Power Backup Inspection", fontsize=11, fontweight='bold', color='#0f172a')
ax.text(8, 40.5, "Customer: Dr. K. V. Satyanarayana | Innespeta (1.8 km away)", fontsize=8.8, color='#334155')
ax.text(8, 38.0, "Schedule: Mon - Sat (8:30 AM - 9:30 AM) • 30 Days Contract", fontsize=8.2, color='#64748b')
ax.text(8, 35.5, "Monthly Payout: ₹6,500  (Escrow Guaranteed)", fontsize=9.2, fontweight='bold', color='#059669')

# Accept / Decline Buttons
btn_acc = patches.FancyBboxPatch((40, 32.5), 12, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor='#10b981', edgecolor='none')
ax.add_patch(btn_acc)
ax.text(46, 34.4, "ACCEPT", fontsize=8.5, fontweight='bold', color='white', ha='center', va='center')

btn_dec = patches.FancyBboxPatch((53, 32.5), 11, 3.8, boxstyle="round,pad=0.2,rounding_size=0.4",
                                facecolor='#f1f5f9', edgecolor='#cbd5e1')
ax.add_patch(btn_dec)
ax.text(58.5, 34.4, "DECLINE", fontsize=8.5, fontweight='bold', color='#64748b', ha='center', va='center')

# Dispatch Item 2: One-Time On-Demand Task
item2_box = patches.FancyBboxPatch((6, 12), 60, 17, boxstyle="round,pad=0.4,rounding_size=0.6",
                                  facecolor='#ffffff', edgecolor='#e2e8f0', linewidth=1.2)
ax.add_patch(item2_box)

onetime_tag = patches.FancyBboxPatch((8, 25.0), 16, 2.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                     facecolor='#f1f5f9', edgecolor='#cbd5e1')
ax.add_patch(onetime_tag)
ax.text(16, 26.2, "ONE-TIME REPAIR", fontsize=7.2, fontweight='bold', color='#475569', ha='center', va='center')

ax.text(8, 22.5, "Short Circuit Diagnosis & Sub-meter Replacement", fontsize=10.5, fontweight='bold', color='#0f172a')
ax.text(8, 19.8, "Customer: M. Rama Rao | Morampudi Junction (2.6 km away)", fontsize=8.5, color='#334155')
ax.text(8, 17.5, "Expected Duration: 1.5 Hours • Emergency Callout", fontsize=8.0, color='#64748b')
ax.text(8, 15.0, "Service Fee: ₹450 (Includes Visiting Charge)", fontsize=8.8, fontweight='bold', color='#059669')

btn_acc2 = patches.FancyBboxPatch((40, 13.5), 12, 3.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                 facecolor='#2563eb', edgecolor='none')
ax.add_patch(btn_acc2)
ax.text(46, 15.2, "ACCEPT", fontsize=8.5, fontweight='bold', color='white', ha='center', va='center')

btn_dec2 = patches.FancyBboxPatch((53, 13.5), 11, 3.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                 facecolor='#f1f5f9', edgecolor='#cbd5e1')
ax.add_patch(btn_dec2)
ax.text(58.5, 15.2, "DECLINE", fontsize=8.5, fontweight='bold', color='#64748b', ha='center', va='center')

ax.text(7, 6.5, "Note: Failure to respond within 90s results in auto-delegation to next ranked artisan.",
        fontsize=7.5, fontstyle='italic', color='#94a3b8')

# ----------------- RIGHT PANEL: Active On-Site OTP Verification (Width 64) -----------------
panel_right = patches.FancyBboxPatch((72, 4), 64, 54, boxstyle="round,pad=0.5,rounding_size=0.8",
                                    facecolor='#ffffff', edgecolor='#e2e8f0', linewidth=1.2)
ax.add_patch(panel_right)

ax.text(75, 54.5, "Active Execution & Security Verification Flow", fontsize=11.5, fontweight='bold', color='#1e293b')
ax.text(75, 52.2, "Two-Sided Cryptographic Token Verification to Prevent Ghost Services", fontsize=8.2, color='#64748b')

# Active Job Summary Box
curr_box = patches.FancyBboxPatch((75, 38), 58, 12, boxstyle="round,pad=0.4,rounding_size=0.6",
                                 facecolor='#eff6ff', edgecolor='#bfdbfe', linewidth=1.2)
ax.add_patch(curr_box)
ax.text(77, 46.5, "CURRENTLY ENGAGED TASK: #TK-8402", fontsize=9.2, fontweight='bold', color='#1e40af')
ax.text(77, 43.8, "Client: Smt. B. Lakshmi Devi | Danavaipeta Main Road", fontsize=8.5, color='#1e293b')
ax.text(77, 41.5, "Service: Main Distribution Board Overhaul & Earth Leakage Fix", fontsize=8.2, color='#475569')
ax.text(77, 39.2, "Status: Worker Arrived On-Site • Awaiting Customer Handshake", fontsize=8.0, fontweight='bold', color='#d97706')

# OTP Verification Card (Center-focused)
otp_container = patches.FancyBboxPatch((75, 12), 58, 24, boxstyle="round,pad=0.5,rounding_size=0.6",
                                      facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.2)
ax.add_patch(otp_container)

ax.text(104, 32.5, "ENTER CUSTOMER VERIFICATION OTP", fontsize=10.5, fontweight='bold', color='#0f172a', ha='center')
ax.text(104, 30.2, "Ask customer for the 4-digit arrival code shown on their consumer app",
        fontsize=7.8, color='#64748b', ha='center')

# 4 OTP input digit squares
otp_digits = ['8', '2', '0', '4']
otp_start_x = 88.5
for i, d in enumerate(otp_digits):
    digit_box = patches.FancyBboxPatch((otp_start_x + i * 8, 20.5), 6.5, 7.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                       facecolor='#ffffff', edgecolor='#2563eb', linewidth=1.8)
    ax.add_patch(digit_box)
    ax.text(otp_start_x + i * 8 + 3.25, 24.25, d, fontsize=18, fontweight='bold', color='#1e293b', ha='center', va='center')

# Submit OTP Button
btn_verify = patches.FancyBboxPatch((85, 14), 38, 4.2, boxstyle="round,pad=0.2,rounding_size=0.4",
                                   facecolor='#2563eb', edgecolor='none')
ax.add_patch(btn_verify)
ax.text(104, 16.1, "CONFIRM TOKEN & COMMENCE TASK", fontsize=9.2, fontweight='bold', color='white', ha='center', va='center')

# Security validation badge at bottom
sec_box = patches.FancyBboxPatch((75, 5.5), 58, 4.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                 facecolor='#ecfdf5', edgecolor='#a7f3d0')
ax.add_patch(sec_box)
ax.text(104, 7.7, "✓ Cryptographic SHA-256 OTP Match: Geofence Locked within 150m",
        fontsize=8.0, fontweight='bold', color='#065f46', ha='center', va='center')

plt.tight_layout()
output_path = 'docs/figures/fig7_worker_portal_ui.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Figure successfully generated at: {output_path}")
