# String smallest(String s) {
#     if (s.length() % 2 == 1) return s;
#     String s1 = smallest(s.substring(0, s.length()/2));
#     String s2 = smallest(s.substring(s.length()/2), s.length());
#     if (s1 < s2) return s1 + s2;
#     else return s2 + s1;
# }

def StringCheck()