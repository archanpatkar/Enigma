from Rotor import Rotor


r = Rotor(0);
r1 = Rotor(0);
r2 = Rotor(0);


o1 = r2.scramble(r1.scramble(r.scramble("a")));
o2 = r2.scramble(r1.scramble(r.scramble("a")));
o3 = r2.scramble(r1.scramble(r.scramble("a")));
o4 = r2.scramble(r1.scramble(r.scramble("a")));

print(o1);
print(o2);
print(o3);
print(o4);