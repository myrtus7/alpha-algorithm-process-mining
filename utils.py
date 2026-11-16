def print_matrix(M, rows=None, cols=None):
    cells = [[str(x) for x in row] for row in M]
    if cols:
        cells.insert(0, [str(c) for c in cols])
    if rows:
        labels = [""] + [str(r) for r in rows] if cols else [str(r) for r in rows]
        cells = [[lab] + row for lab, row in zip(labels, cells)]

    widths = [max(len(row[j]) for row in cells) for j in range(len(cells[0]))]
    for row in cells:
        print("  ".join(c.rjust(w) for c, w in zip(row, widths))) 