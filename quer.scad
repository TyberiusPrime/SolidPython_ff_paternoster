

difference() {
	cube(center = true, size = [22, 22, 44]);
	#translate(v = [0, 0, 11.0000000000]) {
		rotate(a = [0, 90, 0]) {
			cylinder($fn = 64, center = true, h = 100, r = 4.5000000000);
		}
	}
	#translate(v = [0, 0, -11.0000000000]) {
		rotate(a = [90, 0, 0]) {
			cylinder($fn = 64, center = true, h = 100, r = 4.5000000000);
		}
	}
}