from os.path import join

# ARMCC
ARM_PATH = "C:/Work/toolchains/ARMCompiler_5.03_117_Windows"
ARM_BIN = join(ARM_PATH, "bin")
ARM_INC = join(ARM_PATH, "include")
ARM_LIB = join(ARM_PATH, "lib")

ARM_CPPLIB = join(ARM_LIB, "cpplib")
MY_ARM_CLIB = join(ARM_PATH, "lib", "microlib")

# GCC ARM
GCC_ARM_PATH = "C:/Program Files (x86)/GNU Tools ARM Embedded/6.2 2016q4/bin"

# GCC CodeRed
GCC_CR_PATH = "C:/Work/toolchains/LPCXpresso_6.1.4_194/lpcxpresso/tools/bin"

# IAR
IAR_PATH = "C:/Work/toolchains/iar_6_5/arm"

SERVER_ADDRESS = "127.0.0.1"
LOCALHOST = "127.0.0.1"

# This is moved to separate JSON configuration file used by singletest.py
MUTs = {
}