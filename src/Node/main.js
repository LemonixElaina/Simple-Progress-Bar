function display(isDisplayTime, justNow) {
	if (isDisplayTime) {
		const now = Date.now();
		let seconds = Math.floor((now - justNow) / 1000);
		let minutes = Math.floor(seconds / 60);
		let hours = Math.floor(minutes / 60);
		
		if (seconds.toString().length == 1) {
			seconds = '0' + seconds;
		} if (minutes.toString().length == 1) {
			minutes = '0' + minutes;
		} if (hours.toString().length == 1) {
			hours = '0' + hours;
		}

		// 正常碳基生物可读形势(韩国人不算)
		return `${hours}:${minutes}:${seconds}`;
	} else {
		// ''拼接后不显示
		return '';
	}
}


function processBar(char, info = {}) {
	const {
		barLength = 50,
		prompt = 'Downloading ',
		arrow = ' : ',
		milliseconds = 100,
		side = ['[', '] '], // side[1]后面空一个为了给时间留位置
		isChangeLength = true,
		isDisplayTime = true
	} = info;

	if (![1, 5, 10, 20, 25, 50, 100].includes(barLength)) {
		throw new Error('Invalid bar length');
	}
	const justNow = isDisplayTime ? Date.now() : undefined;
	let count = 0;
	let bar, progress;

	if (isChangeLength) {
		bar = [];
	} else {
		bar = Array(barLength).fill(' ');
		// 长度为barLength且元素都为' '的数组
		progress = 0;
	}

	const id = setInterval( () => {
		if (count < 101) {
			process.stdout.write(
				`${ prompt }${ count }%${ arrow }${ side[0] }${ bar.join('') }${ side[1] }${ display(isDisplayTime, justNow) }`
			);
			process.stdout.write('\r'); // 光标移动到开头

			if (count % (100 / barLength) == 0) {
				if (isChangeLength) {
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

	
	return { done: true };
}

module.exports = { processBar }; // 导出
