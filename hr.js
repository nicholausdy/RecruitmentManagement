const createRow = (i,nama, namaBeasiswa, career, social) => {
	let numCell = document.createElement('td');
	numCell.innerText = i;

	let idBeasiswaCell = document.createElement('td');
	idBeasiswaCell.innerText = idBeasiswa;

	let namaBeasiswaCell = document.createElement('td');
	namaBeasiswaCell.innerText = namaBeasiswa;

	let jenisCell = document.createElement('td');
	jenisCell.innerText = jenis;

	let deskripsiCell = document.createElement('td');
	deskripsiCell.innerText = deskripsi;

	let pemberiCell = document.createElement('td');
	pemberiCell.innerText = pemberi;

	let deadlineCell = document.createElement('td');
	deadlineCell.innerText = deadline;

	let penerimaCell = document.createElement('td');
	penerimaCell.innerHTML = `<span class="label label-info pull-left" data-effect="pop" onclick="detail(${idBeasiswa})">lihat details</span>`
	
	let row = document.createElement('tr');
	row.appendChild(numCell);
	row.appendChild(idBeasiswaCell);
	row.appendChild(namaBeasiswaCell);
	row.appendChild(jenisCell);
	row.appendChild(deskripsiCell);
	row.appendChild(pemberiCell);
	row.appendChild(deadlineCell);
	row.appendChild(penerimaCell)

	let table = document.getElementById('tabelProgram');
	table.appendChild(row);
};