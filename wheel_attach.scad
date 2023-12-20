

difference(){
	union() {
		difference() {
			cube(center = true, size = [28, 28, 22]);
			rotate(a = [0, 90, 0]) {
				cylinder($fn = 64, center = true, h = 100, r = 2.8000000000);
			}
		}
		color(alpha = 1.0000000000, c = "blue") {
			translate(v = [0, -12.5000000000, 0]) {
				difference() {
					union() {
						hull() {
							cube(center = true, size = [28, 3, 22]);
							translate(v = [0, -5, 0]) {
								rotate(a = [0, 90, 0]) {
									cylinder($fn = 64, center = true, h = 28, r = 7);
								}
							}
						}
						translate(v = [-2, 0, 0]) {
							translate(v = [0, -5, 0]) {
								rotate(a = [0, 90, 0]) {
									cylinder($fn = 64, center = true, h = 32, r = 7);
								}
							}
						}
						translate(v = [-2.5000000000, 0, 0]) {
							translate(v = [0, -5, 0]) {
								rotate(a = [0, 90, 0]) {
									cylinder($fn = 64, center = true, h = 33, r = 5);
								}
							}
						}
					}
				}
			}
		}
	}
	/* Holes Below*/
	union(){
		union(){
			cube(center = true, size = [21.5000000000, 21.5000000000, 100]);
		}
		color(alpha = 1.0000000000, c = "blue"){
			translate(v = [0, -12.5000000000, 0]){
				union(){
					translate(v = [0, -5, 0]) {
						rotate(a = [0, 90, 0]) {
							cylinder($fn = 64, center = true, h = 100, r = 4.2000000000);
						}
					}
				}
			}
		}
	} /* End Holes */ 
}