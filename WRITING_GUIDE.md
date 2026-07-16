# Schreib-Spickzettel für dieses Thesis-Projekt

Dieser Spickzettel fasst die wichtigsten Befehle zusammen, die du in den Einzeldateien unter `chapters/`, `pages/` und `appendix/` fürs Schreiben brauchst.

## 1. Kapitel und Abschnitte

```tex
\chapter{Einleitung}
\section{Motivation}
\subsection{Forschungsfrage}
```

- `\chapter{...}` erzeugt ein Kapitel.
- `\section{...}` erzeugt einen Abschnitt.
- `\subsection{...}` erzeugt einen Unterabschnitt.

Für Sonderseiten ohne Kapitelnummer wird oft verwendet:

```tex
\chapter*{Abstract}
\phantomsection\addcontentsline{toc}{chapter}{\protect Abstract}
```

## 2. Platzhaltertext

```tex
\bt
```

- `\bt` ist in der Präambel als Kurzform für Blindtext definiert.
- Nutze das nur als Platzhalter und lösche es später wieder.

## 3. Wichtige Mathe-Kurzbefehle

```tex
$\N, \Z, \Q, \R, \C$
```

- `\N` natürliche Zahlen
- `\Z` ganze Zahlen
- `\Q` rationale Zahlen
- `\R` reelle Zahlen
- `\C` komplexe Zahlen

Weitere nützliche Kurzbefehle:

```tex
$\D x, \E^{x}, \I, \1$
```

- `\D` aufrechtes Differential `d`
- `\E` Eulersche Zahl `e`
- `\I` imaginäre Einheit `i`
- `\1` Eins-/Indikatorsymbol

## 4. Vektoren und Operatoren

```tex
$\bs{x}$
$\diag(-,+,+,+)$
$\arsinh(x)$
```

- `\bs{...}` macht mathematische Symbole fett, z. B. für Vektoren.
- `\diag(...)` setzt den Operator `diag` sauber.
- `\arsinh(...)` setzt den Operator `arsinh` sauber.

## 5. Einheiten und Zahlen mit `siunitx`

```tex
\SI{1.23}{\meter}
\SI{299792458}{\meter\per\second}
```

- `\SI{zahl}{einheit}` ist die Standardform für physikalische Größen.
- Einheiten wie `\meter`, `\second`, `\kilogram`, `\kelvin` kannst du direkt verwenden.

Zusätzliche Einheiten, die im Projekt definiert sind:

```tex
\SI{1}{\au}
\SI{4.2}{\ly}
\SI{3}{\parsec}
\SI{10}{\yr}
```

- `\au` astronomische Einheit
- `\ly` Lichtjahr
- `\parsec` Parsec
- `\yr` Jahr

## 6. Formeln

Inline-Formel:

```tex
Die Energie ist durch $E = mc^2$ gegeben.
```

Abgesetzte Formel:

```tex
\begin{align*}
    E &= mc^2 \\
    p &= mv
\end{align*}
```

- Für mehrere ausgerichtete Gleichungen ist `align*` praktisch.
- Mit `*` werden keine Gleichungsnummern gesetzt.

## 7. Bilder

```tex
\begin{figure}[!h]
    \centering
    \includegraphics[width=0.7\linewidth]{figures/beispielbild.png}
    \caption{Beispielabbildung.}
    \label{fig:beispiel}
\end{figure}
```

- Bilder liegen typischerweise im Ordner `figures/`.
- Mit `\label{...}` kannst du später referenzieren.

## 8. Verweise

```tex
Wie in Abbildung~\ref{fig:beispiel} gezeigt, ...
```

- `\label{...}` setzt eine Marke.
- `\ref{...}` verweist auf diese Marke.

Sinnvolle Namensmuster:

- `fig:...` für Abbildungen
- `sec:...` für Abschnitte
- `eq:...` für Gleichungen
- `tab:...` für Tabellen

## 9. Zitate und Literatur

Die Bibliographie wird über `biblatex` eingebunden. Typische Befehle sind:

```tex
\cite{key}
```

Wenn du Literatur verwendest, brauchst du:

- einen Eintrag in `sources/bib_thesis.bib`
- den passenden Schlüssel in `\cite{...}`

## 10. Nützliche Projekt-Makros

Diese Befehle werden vor allem auf Titelseiten genutzt:

```tex
\getAuthor
\getTitleEN
\getTitleDE
\getSupervisorOne
\getSupervisorTwo
```

- Diese Werte kommen aus `preamble_thesis.tex`.
- Für normales Schreiben in Kapiteln brauchst du sie meist nicht.

## 11. Minimalbeispiel für ein Kapitel

```tex
\chapter{Ein Beispielkapitel}

\section{Einführung}
Hier steht dein Fließtext. Mathematische Mengen kannst du als $\R$ oder $\C$ schreiben.

\section{Modell}
Wir betrachten den Vektor $\bs{x}$ und die Metrik $\diag(-,+,+,+)$.

\begin{align*}
    E &= mc^2
\end{align*}

Ein Messwert beträgt \SI{2.5}{\meter}.
```

## 12. Empfehlung fürs tägliche Schreiben

- Nutze `\section` und `\subsection` für die Struktur.
- Nutze `\bt` nur als vorübergehenden Platzhalter.
- Nutze `\SI{...}{...}` konsequent für Einheiten.
- Nutze `\label` und `\ref` direkt beim Schreiben, damit Verweise stabil bleiben.
- Nutze die Kurzbefehle wie `\R`, `\C`, `\bs`, `\diag` für einheitliche Notation.