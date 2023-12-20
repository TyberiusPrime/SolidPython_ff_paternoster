

difference(){
	union() {
		difference() {
			union() {
				cylinder($fn = 150, center = true, h = 7, r = 72.5000000000);
			}
			color(alpha = 1.0000000000, c = "red") {
				cylinder($fn = 150, center = true, h = 8, r = 67.5000000000);
			}
		}
		difference() {
			union() {
				difference() {
					cylinder($fn = 150, center = true, h = 7, r = 16);
				}
				translate(v = [0, 0, 4.0000000000]) {
					color(alpha = 1.0000000000, c = "red") {
						cylinder($fn = 64, center = true, h = 1, r = 13);
					}
				}
			}
		}
		union() {
			color(alpha = 1.0000000000, c = "green") {
				rotate(a = [0, 0, 0]) {
					cube(center = true, size = [145, 7, 7]);
				}
			}
			color(alpha = 1.0000000000, c = "green") {
				rotate(a = [0, 0, 60]) {
					cube(center = true, size = [145, 7, 7]);
				}
			}
			color(alpha = 1.0000000000, c = "green") {
				rotate(a = [0, 0, 120]) {
					cube(center = true, size = [145, 7, 7]);
				}
			}
			color(alpha = 1.0000000000, c = "green") {
				rotate(a = [0, 0, 180]) {
					cube(center = true, size = [145, 7, 7]);
				}
			}
			color(alpha = 1.0000000000, c = "green") {
				rotate(a = [0, 0, 240]) {
					cube(center = true, size = [145, 7, 7]);
				}
			}
			color(alpha = 1.0000000000, c = "green") {
				rotate(a = [0, 0, 300]) {
					cube(center = true, size = [145, 7, 7]);
				}
			}
		}
	}
	/* Holes Below*/
	union(){
		union(){
			union(){
				color(alpha = 1.0000000000, c = "blue") {
					rotate_extrude($fn = 150, angle = 360) {
						translate(v = [-72.5000000000, 0, 0]) {
							circle(r = 2.5000000000);
						}
					}
				}
			}
		}
		union(){
			union(){
				union(){
					cylinder($fn = 64, center = true, h = 8, r = 11.1000000000);
				}
			}
			cylinder($fn = 64, center = true, h = 12, r = 10.6000000000);
		}
	} /* End Holes */ 
}