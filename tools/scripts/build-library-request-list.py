#!/usr/bin/env python3
"""Build the printable list of interlibrary loan requests, grouped by chapter and by priority.

Source of the entries: tools/audits/sources-to-find_master-list_2026-11-26.md (sections A4, A5).
No contact details are stored here; the form leaves blanks for them.

Usage: python3 tools/scripts/build-library-request-list.py [out.pdf]
"""
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, KeepTogether)

D = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("S", D + "DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("SB", D + "DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("SI", D + "DejaVuSerif-Italic.ttf"))
pdfmetrics.registerFontFamily("S", normal="S", bold="SB", italic="SI", boldItalic="SB")

TA = "Appendix"
# (type, citation, needed-first-for, also-for, priority, note)
# type: B book, A article, C book chapter.  priority: 1..4 (see PRIO below)
E = [
 # ---- Chapter 5 ----
 ("A", "Panjwani, A., and H. Xiong. <i>Journal of Economic Behavior &amp; Organization</i> 205 (2023): 648–667. DOI 10.1016/j.jebo.2022.11.017", "5", "", 1, "placed by me"),
 ("A", "Zhou, L., and J. Ge. <i>The Extractive Industries and Society</i> 8, no. 1 (2021): 340–354. DOI 10.1016/j.exis.2020.11.010", "5", TA, 1, "placed by me"),
 ("A", "Lee, J. C. K., and Z. Wen. “Pathways for Greening the Supply of Rare Earth Elements in China.” <i>Nature Sustainability</i> 1, no. 10 (2018): 598–605", "5", "", 1, ""),
 ("A", "Lee, J. C. K., and Z. Wen. <i>Journal of Industrial Ecology</i> 21, no. 5 (2017): 1277–1290", "5", "", 1, ""),
 ("A", "Cano-Urbina, J., C. Clapp, and K. Willardsen. <i>Journal of Housing Economics</i> 43 (2019): 131–156", "5", TA, 1, ""),
 ("A", "Fraser, Nancy. “Behind Marx’s Hidden Abode.” <i>New Left Review</i> 86 (2014): 55–72", "5", "", 1, ""),
 ("B", "Darity, William A., Jr., and A. Kirsten Mullen. <i>From Here to Equality</i>. 2nd ed. Univ. of North Carolina Press, 2022", "5", "3, 8, " + TA, 1, "2nd edition"),
 ("B", "Fraser, Nancy. <i>Cannibal Capitalism</i>. Verso, 2022", "5", "2", 1, ""),
 ("B", "Gawande, Atul. <i>Being Mortal</i>. Metropolitan Books, 2014", "5", "", 1, ""),
 ("B", "Schneider, Andrew, and David McCumber. <i>An Air That Kills</i>. Putnam, 2004", "5", TA, 1, ""),
 ("B", "Conley, Dalton. <i>Being Black, Living in the Red</i>. Univ. of California Press, 1999", "5", "8", 1, ""),
 ("B", "Parfit, Derek. <i>Reasons and Persons</i>. Oxford Univ. Press, 1984", "5", "6, " + TA, 1, ""),
 ("B", "Pettit, Philip. <i>Republicanism: A Theory of Freedom and Government</i>. Oxford Univ. Press, 1997", "5", "", 1, ""),
 ("B", "Skinner, Quentin. <i>Liberty Before Liberalism</i>. Cambridge Univ. Press, 1998", "5", "", 1, ""),
 ("B", "Hacker, Jacob S. <i>The Great Risk Shift</i>. Oxford Univ. Press, 2006", "5", "", 1, ""),
 ("B", "Bullard, Robert D. <i>Dumping in Dixie</i>. Westview Press, 1990", "5", TA, 1, ""),
 ("B", "Martínez-Alier, Joan. <i>The Environmentalism of the Poor</i>. Edward Elgar, 2002", "5", "", 1, "best guess at the work meant"),
 ("B", "Kapp, K. William. <i>The Social Costs of Private Enterprise</i>. Harvard Univ. Press, 1950", "5", "6", 1, ""),
 # ---- Appendix, checked claims ----
 ("A", "Slade, M. E., and H. Thille. <i>Annual Review of Resource Economics</i> 1 (2009): 239–260", TA, "", 1, ""),
 ("A", "Mudliar, P., and T. Koontz. <i>Society &amp; Natural Resources</i> 34, no. 5 (2021): 639–658", TA, "6", 1, ""),
 ("A", "Broome, John. “Discounting the Future.” <i>Philosophy &amp; Public Affairs</i> 23, no. 2 (1994): 128–156", TA, "6", 1, ""),
 ("A", "Bernhardt, E. S., and M. A. Palmer. <i>Annals of the New York Academy of Sciences</i> 1223 (2011): 39–57", TA, "6", 1, ""),
 ("A", "Loomes, G., and R. Sugden. <i>The Economic Journal</i> 92, no. 368 (1982): 805–824", TA, "", 1, ""),
 ("A", "Asare, B. Y.-A., et al. “Rotation Work in the Resources Sector.” <i>Psychology &amp; Health</i> 40, no. 1: 17–46 (online 2023)", TA, "", 1, ""),
 ("A", "Barnosky, A. D., et al. <i>Nature</i> 486 (2012): 52–58", TA, "", 1, ""),
 ("A", "Howarth, R. B., and R. B. Norgaard. “Environmental Valuation under Sustainable Development.” <i>American Economic Review</i> 82, no. 2 (1992): 473–477", TA, "", 1, ""),
 ("C", "El Serafy, Salah. “The Proper Calculation of Income from Depletable Natural Resources.” In Ahmad, El Serafy and Lutz, eds., <i>Environmental Accounting for Sustainable Development</i>. World Bank, 1989", TA, "6", 1, "chapter only"),
 ("A", "Lenton, T. M., et al. <i>PNAS</i> 105, no. 6 (2008): 1786–1793", TA, "", 1, ""),
 ("A", "Solomon, S., et al. <i>PNAS</i> 106, no. 6 (2009): 1704–1709", TA, "", 1, ""),
 ("A", "Lindberg, T. T., et al. <i>PNAS</i> 108, no. 52 (2011): 20929–20934", TA, "", 1, ""),
 ("A", "Kilian, Lutz. <i>American Economic Review</i> 99, no. 3 (2009): 1053–1069", TA, "", 1, ""),
 ("A", "Dwyer-Lindgren, L., et al. <i>JAMA Internal Medicine</i> 177, no. 7 (2017): 1003–1011", TA, "6", 1, ""),
 ("A", "Pindyck, Robert S. “Volatility and Commodity Price Dynamics.” <i>The Energy Journal</i> 29, no. 1 (2008): 1–26", TA, "", 1, ""),
 ("A", "Arrow, K. J., and A. C. Fisher. <i>Quarterly Journal of Economics</i> 88, no. 2 (1974): 312–319", TA, "6", 1, ""),
 ("A", "Henry, Claude. <i>American Economic Review</i> 64, no. 6 (1974): 1006–1012", TA, "6", 1, ""),
 ("B", "Rawls, John. <i>A Theory of Justice</i>. Harvard Univ. Press, 1971", TA, "", 1, "1971 edition only"),
 ("B", "Keefe, Patrick Radden. <i>Empire of Pain</i>. Doubleday, 2021", TA, "2", 1, ""),
 ("B", "Dasgupta, P. S., and G. M. Heal. <i>Economic Theory and Exhaustible Resources</i>. Cambridge Univ. Press, 1979", TA, "", 1, ""),
 ("B", "Broome, John. <i>Climate Matters</i>. W. W. Norton, 2012", TA, "6", 1, ""),
 ("B", "Broome, John. <i>Counting the Cost of Global Warming</i>. White Horse Press, 1992", TA, "6", 1, ""),
 ("B", "Sen, Amartya. <i>Development as Freedom</i>. Knopf, 1999", TA, "6", 1, ""),
 ("B", "Sen, Amartya. <i>Commodities and Capabilities</i>. North-Holland, 1985", TA, "", 1, ""),
 ("B", "Nussbaum, Martha C. <i>Women and Human Development</i>. Cambridge Univ. Press, 2000", TA, "", 1, ""),
 ("B", "Mishan, E. J. <i>Cost-Benefit Analysis</i>. 1971", TA, "", 1, ""),
 ("B", "Bockstael, N. E., and K. E. McConnell. <i>Environmental and Resource Valuation with Revealed Preferences</i>. Springer, 2007", TA, "", 1, ""),
 ("B", "Lewis, David. <i>Counterfactuals</i>. Harvard Univ. Press, 1973", TA, "", 1, ""),
 ("B", "Hicks, J. R. <i>Value and Capital</i>. Oxford Univ. Press, 1939", TA, "", 1, ""),
 ("B", "Samuelson, Paul A. <i>Foundations of Economic Analysis</i>. Harvard Univ. Press, 1947", TA, "", 1, "may be the wrong work"),
 ("B", "Savage, Leonard J. <i>The Foundations of Statistics</i>. Wiley, 1954", TA, "6", 1, ""),
 ("B", "Dixit, A. K., and R. S. Pindyck. <i>Investment under Uncertainty</i>. Princeton Univ. Press, 1994", TA, "", 1, ""),
 # ---- Appendix, placed 2026-11-27 (owed from the reconciliation's hand check) ----
 ("A", "Viscusi, W. Kip. “The Value of Risks to Life and Health.” <i>Journal of Economic Literature</i> 31, no. 4 (1993): 1912–1946", TA, "", 1, "placed 2026-11-27"),
 ("A", "Cobb, Charles W., and Paul H. Douglas. “A Theory of Production.” <i>American Economic Review</i> 18, no. 1, supplement (1928): 139–165", TA, "", 4, "placed 2026-11-27"),
 ("A", "Costanza, Robert, et al. “The Value of the World’s Ecosystem Services and Natural Capital.” <i>Nature</i> 387 (1997): 253–260. DOI 10.1038/387253a0", TA, "", 4, "placed 2026-11-27"),
 ("B", "Benjamin, Ruha. <i>Race After Technology</i>. Polity, 2019", TA, "", 4, "placed 2026-11-27"),
 ("B", "Du Bois, W. E. B. <i>Black Reconstruction in America, 1860–1880</i>. Harcourt, Brace, 1935", TA, "", 4, "placed 2026-11-27; any reprint"),
 ("B", "Habermas, Jürgen. <i>The Theory of Communicative Action</i>, vol. 1. Translated by Thomas McCarthy. Beacon Press, 1984", TA, "", 4, "placed 2026-11-27; volume 1 only"),
 ("B", "Hickel, Jason. <i>Less Is More</i>. William Heinemann, 2020", TA, "", 4, "placed 2026-11-27"),
 ("B", "Nordhaus, William D., and Joseph Boyer. <i>Warming the World</i>. MIT Press, 2000", TA, "", 4, "placed 2026-11-27"),
 ("B", "North, Douglass C. <i>Institutions, Institutional Change and Economic Performance</i>. Cambridge Univ. Press, 1990", TA, "", 4, "placed 2026-11-27"),
 ("B", "Putnam, Robert D. <i>Bowling Alone</i>. Simon &amp; Schuster, 2000", TA, "", 4, "placed 2026-11-27"),
 # ---- Chapter 2 ----
 ("B", "Fishback, Price V. <i>Soft Coal, Hard Choices</i>. Oxford Univ. Press, 1992", "2", "", 2, ""),
 ("B", "Harvey, David. <i>The New Imperialism</i>. Oxford Univ. Press, 2003", "2", "3", 2, ""),
 ("B", "Derickson, Alan. <i>Black Lung: Anatomy of a Public Health Disaster</i>. Cornell Univ. Press, 1998", "2", "8", 2, ""),
 ("B", "Mazzucato, Mariana. <i>The Value of Everything</i>. Allen Lane, 2018", "2", "3, " + TA, 2, ""),
 ("B", "White, Theodore H. <i>The Making of the President 1960</i>. Atheneum, 1961", "2", "", 2, "placed 2026-11-27"),
 # ---- Chapter 4 ----
 ("B", "Ndikumana, Léonce, and James K. Boyce. <i>Africa’s Odious Debts</i>. Zed Books, 2011", "4", "", 2, ""),
 ("B", "Zucman, Gabriel. <i>The Hidden Wealth of Nations</i>. Univ. of Chicago Press, 2015", "4", "", 2, ""),
 # ---- Chapter 3 ----
 ("A", "Hardin, Garrett. “The Tragedy of the Commons.” <i>Science</i> 162, no. 3859 (1968): 1243–1248", "3", "", 2, ""),
 ("B", "Ostrom, Elinor. <i>Governing the Commons</i>. Cambridge Univ. Press, 1990", "3", "6, 9, " + TA, 2, ""),
 # ---- Chapter 10 ----
 ("B", "Kimmerer, Robin Wall. <i>Braiding Sweetgrass</i>. Milkweed Editions, 2013", "10", "", 2, "best guess at the work meant"),
 ("B", "Simpson, Leanne Betasamosake. <i>As We Have Always Done</i>. Univ. of Minnesota Press, 2017", "10", "", 2, "best guess at the work meant"),
 ("B", "Dunbar-Ortiz, Roxanne. <i>An Indigenous Peoples’ History of the United States</i>. Beacon Press, 2014", "10", "", 2, "best guess at the work meant"),
 ("B", "Deloria, Vine, Jr. <i>Custer Died for Your Sins</i>. Macmillan, 1969", "10", "", 2, "best guess at the work meant"),
 ("B", "Coulthard, Glen Sean. <i>Red Skin, White Masks</i>. Univ. of Minnesota Press, 2014", "10", TA, 2, ""),
 ("B", "Camus, Albert. <i>The Myth of Sisyphus</i>. Translated by Justin O’Brien. 1955", "10", "", 2, "English translation"),
 # ---- Chapter 6 ----
 ("A", "Solow, Robert M. “Intergenerational Equity and Exhaustible Resources.” <i>Review of Economic Studies</i> 41 (1974): 29–45", "6", TA, 3, ""),
 ("A", "Ramsey, F. P. “A Mathematical Theory of Saving.” <i>The Economic Journal</i> 38, no. 152 (1928): 543–559", "6", "", 3, ""),
 ("A", "Savage, L. J. “The Theory of Statistical Decision.” <i>Journal of the American Statistical Association</i> 46, no. 253 (1951): 55–67", "6", TA, 3, ""),
 # ---- Chapter 7 ----
 ("B", "Lehner, Mark, and Zahi Hawass. <i>Giza and the Pyramids</i>. Univ. of Chicago Press, 2017", "7", "", 3, "best guess at the work meant"),
 ("B", "Sima Qian. <i>Records of the Grand Historian</i>", "7", "", 3, "any English translation"),
 ("A", "Wittenberg, L. J., J. F. Santarius, and G. L. Kulcinski. “Lunar Source of ³He for Commercial Fusion Power.” <i>Fusion Technology</i> 10 (1986): 167–178", "7", "", 3, ""),
 # ---- Chapter 8 ----
 ("A", "Hendryx, M., et al. “Self-Reported Cancer Rates in Two Rural Areas of West Virginia with and without Mountaintop Coal Mining.” <i>Journal of Community Health</i> 37 (2012): 320–327", "8", "", 3, ""),
 ("A", "Tullock, Gordon. “The Welfare Costs of Tariffs, Monopolies, and Theft.” <i>Western Economic Journal</i> 5, no. 3 (1967): 224–232", "8", "9", 3, ""),
 ("A", "Wagner, Gernot, et al. “Eight Priorities for Calculating the Social Cost of Carbon.” <i>Nature</i> 590 (2021): 548–550", "8", "", 3, ""),
 ("B", "Buchanan, James M., and Gordon Tullock. <i>The Calculus of Consent</i>. Univ. of Michigan Press, 1962", "8", "9", 3, ""),
 ("B", "Ellison, Ralph. <i>Invisible Man</i>. Random House, 1952", "8", "", 3, ""),
 ("B", "Fanon, Frantz. <i>Black Skin, White Masks</i>", "8", "", 3, "English translation"),
 # ---- Chapter 9 ----
 ("A", "Coase, Ronald H. “The Problem of Social Cost.” <i>Journal of Law and Economics</i> 3 (1960): 1–44", "9", TA, 3, ""),
 ("B", "Gardiner, Stephen M. <i>A Perfect Moral Storm</i>. Oxford Univ. Press, 2011", "9", "", 3, ""),
 ("B", "Nozick, Robert. <i>Anarchy, State, and Utopia</i>. Basic Books, 1974", "9", "", 3, ""),
 ("B", "Christophers, Brett. <i>Rentier Capitalism</i>. Verso, 2020", "9", "", 3, ""),
 ("B", "Christophers, Brett. <i>The Price Is Wrong</i>. Verso, 2024", "9", "5", 3, "whole book"),
 ("B", "Chang, Ha-Joon. <i>Kicking Away the Ladder</i>. Anthem Press, 2002", "9", "", 3, ""),
 ("B", "Olson, Mancur. <i>The Logic of Collective Action</i>. Harvard Univ. Press, 1965", "9", TA, 3, ""),
 ("B", "Susskind, Daniel. <i>Growth: A Reckoning</i>. Harvard Univ. Press, 2024", "9", "", 3, ""),
 # ---- Appendix reference list (never opened) ----
 ("A", "Akerlof, George A. “The Market for ‘Lemons’.” <i>Quarterly Journal of Economics</i> 84, no. 3 (1970): 488–500", TA, "", 4, ""),
 ("A", "Brennan, M. J., and E. S. Schwartz. “Evaluating Natural Resource Investments.” <i>The Journal of Business</i> 58, no. 2 (1985): 135–157", TA, "", 4, ""),
 ("A", "Mandelbrot, Benoit. “The Variation of Certain Speculative Prices.” <i>Journal of Business</i> 36, no. 4 (1963): 394–419", TA, "", 4, ""),
 ("A", "Mann, Michael. “The Autonomous Power of the State.” <i>European Journal of Sociology</i> 25, no. 2 (1984): 185–213", TA, "", 4, ""),
 ("A", "Stigler, George J. “The Theory of Economic Regulation.” <i>Bell Journal of Economics and Management Science</i> 2, no. 1 (1971): 3–21", TA, "", 4, ""),
 ("A", "Atkinson, Anthony B. “On the Measurement of Inequality.” <i>Journal of Economic Theory</i> 2, no. 3 (1970): 244–263", TA, "", 4, ""),
 ("A", "Bergson, Abram. “A Reformulation of Certain Aspects of Welfare Economics.” <i>Quarterly Journal of Economics</i> 52, no. 2 (1938): 310–334", TA, "", 4, ""),
 ("A", "Hong, Lu, and Scott E. Page. “Groups of Diverse Problem Solvers Can Outperform Groups of High-Ability Problem Solvers.” <i>PNAS</i> 101, no. 46 (2004): 16385–16389", TA, "", 4, ""),
 ("B", "Anderson, Chris. <i>The Long Tail</i>. Hyperion, 2006", TA, "", 4, ""),
 ("B", "Anderson, Elizabeth. <i>Private Government</i>. Princeton Univ. Press, 2017", TA, "", 4, ""),
 ("B", "Brown Weiss, Edith. <i>In Fairness to Future Generations</i>. Transnational Publishers, 1989", TA, "", 4, ""),
 ("B", "Desmond, Matthew. <i>Evicted</i>. Crown, 2016", TA, "", 4, ""),
 ("B", "Hess, Charlotte, and Elinor Ostrom, eds. <i>Understanding Knowledge as a Commons</i>. MIT Press, 2007", TA, "", 4, ""),
 ("B", "Hyman, Louis. <i>Debtor Nation</i>. Princeton Univ. Press, 2011", TA, "", 4, ""),
 ("B", "Rothstein, Richard. <i>The Color of Law</i>. Liveright, 2017", TA, "", 4, ""),
 ("B", "Sugrue, Thomas J. <i>The Origins of the Urban Crisis</i>. Princeton Univ. Press, 1996", TA, "", 4, ""),
 ("B", "Taylor, Keeanga-Yamahtta. <i>Race for Profit</i>. Univ. of North Carolina Press, 2019", TA, "", 4, ""),
 ("B", "Wolfe, Patrick. <i>Settler Colonialism and the Transformation of Anthropology</i>. Cassell, 1999", TA, "", 4, ""),
 ("B", "Tönnies, Ferdinand. <i>Community and Society</i>. Translated by Charles P. Loomis. Michigan State Univ. Press, 1957", TA, "", 4, "English translation"),
 ("B", "Kant, Immanuel. <i>Groundwork of the Metaphysics of Morals</i>. Translated by Mary Gregor and Jens Timmermann. Cambridge Univ. Press", TA, "", 4, "this translation"),
 ("B", "Acemoglu, Daron, and James A. Robinson. <i>Why Nations Fail</i>. Crown Business, 2012", TA, "", 4, ""),
 ("B", "Coleman, James S. <i>Foundations of Social Theory</i>. Harvard Univ. Press, 1990", TA, "", 4, ""),
 ("B", "Crawford, Kate. <i>Atlas of AI</i>. Yale Univ. Press, 2021", TA, "", 4, ""),
 ("B", "Daily, Gretchen C., ed. <i>Nature’s Services</i>. Island Press, 1997", TA, "", 4, ""),
 ("B", "Embrechts, P., C. Klüppelberg, and T. Mikosch. <i>Modelling Extremal Events for Insurance and Finance</i>. Springer, 1997", TA, "", 4, ""),
 ("B", "Federici, Silvia. <i>Caliban and the Witch</i>. Autonomedia, 2004", TA, "", 4, ""),
 ("B", "Folland, Gerald B. <i>Real Analysis</i>. 2nd ed. Wiley, 1999", TA, "", 4, ""),
 ("B", "Fricker, Miranda. <i>Epistemic Injustice</i>. Oxford Univ. Press, 2007", TA, "", 4, ""),
 ("B", "Jacobs, Jane. <i>The Death and Life of Great American Cities</i>. Random House, 1961", TA, "", 4, ""),
 ("B", "Klinenberg, Eric. <i>Palaces for the People</i>. Crown, 2018", TA, "", 4, ""),
 ("B", "O’Neil, Cathy. <i>Weapons of Math Destruction</i>. Crown, 2016", TA, "", 4, ""),
 ("B", "Patel, Raj, and Jason W. Moore. <i>A History of the World in Seven Cheap Things</i>. Univ. of California Press, 2017", TA, "", 4, ""),
 ("B", "Reilly, Benjamin. <i>Democracy and Diversity</i>. Oxford Univ. Press, 2001", TA, "", 4, ""),
 ("B", "Royden, H. L. <i>Real Analysis</i>. 3rd ed. Macmillan, 1988", TA, "", 4, ""),
 ("B", "Stiglitz, Joseph E. <i>Economics of the Public Sector</i>. 3rd ed. W. W. Norton, 2000", TA, "", 4, ""),
 ("B", "Taleb, Nassim Nicholas. <i>The Black Swan</i>. Random House, 2007", TA, "", 4, ""),
 ("B", "Tilly, Charles. <i>Coercion, Capital and European States, AD 990–1990</i>. Blackwell, 1990", TA, "", 4, ""),
 ("B", "Tirole, Jean. <i>The Theory of Industrial Organization</i>. MIT Press, 1988", TA, "", 4, ""),
 ("B", "Tuan, Yi-Fu. <i>Space and Place</i>. Univ. of Minnesota Press, 1977", TA, "", 4, ""),
 ("B", "Weston, Kath. <i>Families We Choose</i>. Columbia Univ. Press, 1991", TA, "", 4, ""),
 ("B", "Esping-Andersen, Gøsta. <i>The Three Worlds of Welfare Capitalism</i>. Princeton Univ. Press, 1990", TA, "", 4, ""),
 ("B", "Mosteller, F., and J. W. Tukey. <i>Data Analysis and Regression</i>. Addison-Wesley, 1977", TA, "", 4, ""),
]

PRIO = {
 1: ("First", "Chapter 5 and the Technical Appendix. With Chapter 1, these are the sample that goes out first."),
 2: ("Second", "Chapters 2, 4, 3 and 10, the next to be drafted, in that order."),
 3: ("Third", "Chapters 6, 7, 8 and 9, drafted after those."),
 4: ("Fourth", "Works on the appendix’s reference list that have not yet been opened. Nothing waits on them."),
}
CH_ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", TA]
CH_TITLE = {"2": "Chapter 2, The Miner", "3": "Chapter 3, The Waterman", "4": "Chapter 4, The Existence Proof",
            "5": "Chapter 5, The Accountability Gap", "6": "Chapter 6, Three Ways of Counting",
            "7": "Chapter 7, On Other Worlds", "8": "Chapter 8, What Things Actually Cost",
            "9": "Chapter 9, Pricing Honestly", "10": "Chapter 10, Common Bonds", TA: "Technical Appendix"}
DRAFT_ORDER = ["5", TA, "2", "4", "3", "10", "6", "7", "8", "9"]
TYPE = {"B": "Book", "A": "Article", "C": "Chapter"}

rows = [dict(n=i + 1, t=t, c=c, ch=ch, also=a, p=p, note=nt) for i, (t, c, ch, a, p, nt) in enumerate(E)]

body = ParagraphStyle("b", fontName="S", fontSize=8.2, leading=10.4)
small = ParagraphStyle("s", fontName="S", fontSize=7.4, leading=9.4)
h1 = ParagraphStyle("h1", fontName="SB", fontSize=14, leading=18, spaceAfter=4)
h2 = ParagraphStyle("h2", fontName="SB", fontSize=10.5, leading=13, spaceBefore=9, spaceAfter=3)
para = ParagraphStyle("p", fontName="S", fontSize=9, leading=12.5, spaceAfter=5)


def short(ch):
    return "App." if ch == TA else "Ch " + ch


def places(r):
    return [r["ch"]] + [x.strip() for x in r["also"].split(",") if x.strip()]


def fmt(pl):
    pl = sorted(pl, key=CH_ORDER.index)
    chs = [x for x in pl if x != TA]
    out = ("Ch " + ", ".join(chs)) if chs else ""
    if TA in pl:
        out = (out + ", " if out else "") + "App."
    return out


def table(items, here=None):
    """here: the chapter this table sits under (Part 1), or None (Part 2: show every place)."""
    head = ["No.", "Kind", "Requested item", "Also used in" if here else "Used in", "Priority", "Here"]
    data = [[Paragraph("<b>%s</b>" % h, small) for h in head]]
    for r in items:
        cite = r["c"] + (" <b>[%s]</b>" % r["note"] if r["note"] else "")
        pl = [x for x in places(r) if x != here]
        data.append([Paragraph(str(r["n"]), small), Paragraph(TYPE[r["t"]], small), Paragraph(cite, body),
                     Paragraph(fmt(pl), small), Paragraph(PRIO[r["p"]][0], small), ""])
    t = Table(data, colWidths=[0.36 * inch, 0.56 * inch, 4.4 * inch, 0.88 * inch, 0.6 * inch, 0.4 * inch], repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, 0), colors.Color(.9, .9, .9)),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]))
    return t


def counts(items):
    b = sum(1 for r in items if r["t"] == "B"); a = len(items) - b
    parts = []
    if b:
        parts.append("%d book%s" % (b, "" if b == 1 else "s"))
    if a:
        parts.append("%d article%s" % (a, "" if a == 1 else "s"))
    return "%d item%s (%s)" % (len(items), "" if len(items) == 1 else "s", ", ".join(parts))


def key(r):
    return (r["p"], {"A": 0, "C": 0, "B": 1}[r["t"]], r["n"])


def footer(canvas, doc):
    canvas.setFont("S", 7.5)
    canvas.drawString(0.6 * inch, 0.45 * inch, "Interlibrary loan requests placed 2026-11-26 and 27")
    canvas.drawRightString(letter[0] - 0.6 * inch, 0.45 * inch, "Page %d" % doc.page)


def find(frag):
    r = [x for x in rows if frag in x["c"]]
    assert len(r) == 1, frag
    return r[0]


# Part 1: requests that may be wrong, or where a wrong edition would be. (fragment of citation, what to know)
WRONG = [
 ("Foundations of Economic Analysis", "Probably the wrong work. My source gives only “Samuelson 1948,” with no "
  "title. The 1947 book was requested as a guess; the work meant is more likely his 1948 article, “Consumption "
  "Theory in Terms of Revealed Preference,” <i>Economica</i> 15, no. 60: 243–253. Please hold the book until I confirm."),
]
GUESS = [
 ("Braiding Sweetgrass", "The chapter names the author only. This title was my best guess."),
 ("As We Have Always Done", "The chapter names the author only. This title was my best guess."),
 ("Indigenous Peoples", "The chapter names the author only. This title was my best guess."),
 ("Custer Died", "The chapter names the author only. This title was my best guess."),
 ("Giza and the Pyramids", "The chapter names the two excavators, not a book. Their joint book was my best guess."),
 ("Environmentalism of the Poor", "The chapter names the author only. This title was my best guess."),
]
EDITION = [
 ("A Theory of Justice", "The original 1971 edition only. The 1999 revised edition has different pages and wording."),
 ("From Here to Equality", "The second edition (2022) only."),
 ("Groundwork of the Metaphysics", "The Gregor and Timmermann translation (Cambridge) only."),
 ("Community and Society", "The Loomis translation (1957). A German-language copy is not needed."),
 ("Records of the Grand Historian", "Any published English translation will do. An original-language copy is not needed."),
 ("Black Skin, White Masks", "Any published English translation. A French-language copy is not needed."),
 ("Myth of Sisyphus", "The O’Brien English translation. A French-language copy is not needed."),
 ("The Proper Calculation of Income", "The one chapter only, not the whole volume."),
]


def check_table(pairs):
    data = [[Paragraph("<b>%s</b>" % h, small) for h in ("No.", "Requested item", "What to know")]]
    for frag, note in pairs:
        r = find(frag)
        data.append([Paragraph(str(r["n"]), small), Paragraph(r["c"], body), Paragraph(note, body)])
    t = Table(data, colWidths=[0.36 * inch, 3.3 * inch, 3.64 * inch], repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, 0), colors.Color(.9, .9, .9)),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]))
    return t


def build(out):
    S = []
    nb = sum(1 for r in rows if r["t"] == "B")
    S.append(Paragraph("Interlibrary loan requests: what to check first, priorities, and where each is used", h1))
    S.append(Paragraph("Name: ____________________________ &nbsp;&nbsp;&nbsp; Student ID: __________________ &nbsp;&nbsp;&nbsp; "
                       "Date: ______________<br/><br/>Pickup location: ____________________ &nbsp;&nbsp;&nbsp; "
                       "Email for articles: ______________________________", para))
    S.append(Paragraph("The %d items below were requested through the library’s online form on November 26, 2026 "
                       "(%d books, %d articles, one of them a book chapter). They support a book manuscript of ten "
                       "chapters and a technical appendix. Each item has one number, used in all three parts. "
                       "<b>Part 1</b> lists requests that may be wrong, so nobody searches for the wrong thing. "
                       "<b>Part 2</b> lists every item once, by how soon it is needed. <b>Part 3</b> lists the items "
                       "by where they are used in the book. The last column in Parts 2 and 3 is a box to tick when "
                       "an item arrives." % (len(rows), nb, len(rows) - nb), para))
    S.append(Paragraph("Part 1. Please check these first", h1))
    S.append(Paragraph("1a. Probably the wrong work: please hold", h2))
    S.append(check_table(WRONG))
    S.append(Paragraph("1b. The title was a best guess: I will confirm each", h2))
    S.append(Paragraph("These are worth filling if they are easy to get. If one is hard to find, please ask me "
                       "before spending time on it.", para))
    S.append(check_table(GUESS))
    S.append(Paragraph("1c. The edition or translation matters", h2))
    S.append(Paragraph("These requests are right, but a different edition would not serve.", para))
    S.append(check_table(EDITION))
    S.append(Paragraph("1d. A possible duplicate", h2))
    S.append(Paragraph("My own log counted 127 submissions, and this list has %d distinct items. If one item "
                       "appears twice in your queue, the second is a duplicate and can be cancelled." % len(rows), para))
    S.append(PageBreak())
    S.append(Paragraph("Part 2. By priority", h1))
    S.append(Paragraph("Within a priority, articles matter as much as books; they are listed first only because they "
                       "arrive by email. A note in square brackets marks an edition or translation that matters, or a "
                       "title that was a best guess.", para))
    for p in (1, 2, 3, 4):
        its = [r for r in rows if r["p"] == p]
        S.append(Paragraph("%s priority: %s" % (PRIO[p][0], counts(its)), h1))
        S.append(Paragraph(PRIO[p][1], para))
        for ch in DRAFT_ORDER:
            sub = sorted([r for r in its if r["ch"] == ch], key=key)
            if not sub:
                continue
            S.append(Paragraph("%s: %s" % (CH_TITLE[ch], counts(sub)), h2))
            S.append(table(sub))
    S.append(PageBreak())
    S.append(Paragraph("Part 3. By where each item is used in the book", h1))
    S.append(Paragraph("An item used in more than one place is listed under each, so this part has more rows than "
                       "items. Chapter 1 has no requests: it names no outside work.", para))
    for ch in CH_ORDER:
        its = sorted([r for r in rows if ch in places(r)], key=key)
        S.append(KeepTogether([Paragraph("%s: %s" % (CH_TITLE[ch], counts(its)), h2)]))
        S.append(table(its, here=ch))
    doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                            topMargin=0.6 * inch, bottomMargin=0.7 * inch,
                            title="Interlibrary loan requests", author="")
    doc.build(S, onFirstPage=footer, onLaterPages=footer)
    print(out, len(rows), "items;", nb, "books")


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "tools/audits/library-requests_by-chapter-and-priority_2026-11-26.pdf")
