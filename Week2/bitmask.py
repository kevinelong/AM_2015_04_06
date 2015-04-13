class permissions():
    READ = 4
    WRITE = 2
    EXECUTE = 1

    def __init__(self):
        self.permissions = 0

    def allow(self, permission):
        self.permissions = self.permissions | permission

    def revoke(self, permission):
        self.permissions = self.permissions & ~permission

    def can(self, permission):
        return permission & self.permissions

    def __str__(self):
        return format(self.permissions,"#010b")


p = permissions()
print(p)

p.allow(p.READ)
print(p)
p.allow(p.WRITE)
print(p)
p.allow(p.EXECUTE)
print(p)
p.revoke(p.WRITE)
print(p)

print(p)
# OUTPUTS:
# 0b00000000
# 0b00000100
# 0b00000110
# 0b00000111
# 0b00000101
# 0b00000101