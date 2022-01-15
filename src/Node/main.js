function processBar(char, info) {
	const {
		barLength = 50,
		prompt = 'Downloading ',
		arrow = ' : ',
		milliseconds = 100,
		side = ['[', ']'],
		changeLength = true
	} = info;
	let count = 0;
	let bar, progress;
	
	if (![1, 5, 10, 20, 25, 50, 100].includes(barLength)) {
		throw new Error('Invalid bar length');
	}

	if (changeLength) {
		bar = [];
	} else {
		bar = Array(barLength).fill(' ');
		// 包含50个空格的数组
		progress = 0;
	}

	const id = setInterval( () => {
		if (count < 101) {
			process.stdout.write(
				`${ prompt }${ count }%${ arrow }${ side[0] }${ bar.join('') }${ side[1] }`
			);
			process.stdout.write('\r'); // 光标移动到开头

			if (count % (100 / barLength) == 0) {
				if (changeLength) {
					bar.push(char);
				} else {
					bar[progress] = char;
					progress++;
				}
			}
			count++;
		} else {
			clearInterval(id); // 停止循环
		}
	}, milliseconds );
}

module.exports = { processBar }; // 导出
