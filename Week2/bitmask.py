class permissions():
    READ = 4
    WRITE = 2
    EXECUTE = 1

    def __init__(self):
        self.permissions = 0

    def allow(self, permission):
        #USE "OR" (vertical bar) to set a bit
        self.permissions = self.permissions | permission

    def revoke(self, permission):
        #USE "AND" (ampersand) and "NOT" (tilde)
        # to invert input and unset a bit
        self.permissions = self.permissions & ~permission

    def can(self, permission):
        #USE "AND" (ampersand) check a bit
        # It will be the value of the bit 1,2,4,8 etc if set
        # compare to zero so as to return true only if the bit is set
        return (permission & self.permissions) != 0

    def __str__(self):
        #Use format to create padded binary output
        return format(self.permissions, "#010b") + " --> " + str(self.permissions)

# LOGIC TRUTH TABLE

# | OR
#       0 1
#
#   0   0 1
#   1   1 1

# & AND
#       0 1
#
#   0   0 0
#   1   0 1

# ~ NOT
#
#   0   1
#   1   0

# 6 3 1
# 4 2 6 8 4 2 1
# -------------
# 0 0 0 0 1 1 1 -> decimal 7 showing 4+2+1 all three set
p = permissions()
print(p)
print("CAN READ? " + str(p.can(p.READ)))

p.allow(p.READ)
print(p)

p.allow(p.WRITE)
print(p)

p.allow(p.EXECUTE)
print(p)

p.revoke(p.WRITE)
print(p)

print("CAN READ? " + str(p.can(p.READ)))
# OUTPUTS:
# 0b00000000 --> 0
# CAN READ? False
# 0b00000100 --> 4
# 0b00000110 --> 6
# 0b00000111 --> 7
# 0b00000101 --> 5
# CAN READ? True