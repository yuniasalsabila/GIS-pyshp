import shapefile

w=shapefile.Writer('./soal10',shapeType=shapefile.POLYGON)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("crot","dua")
w.record("crit","tiga")
w.record("cret","empat")
w.record("crat","lima")
w.record("crat","enam")

w.poly([[[1,1],[2,3],[4,3],[3,1]]])
w.poly([[[1,4],[2,6],[4,6],[3,4]]])
w.poly([[[1,8],[2,10],[4,10],[3,8]]])
w.poly([[[6,1],[7,4],[9,4],[8,1]]])
w.poly([[[6,5],[7,8],[9,8],[8,5]]])
w.poly([[[10,1],[11,4],[13,4],[12,1]]])

