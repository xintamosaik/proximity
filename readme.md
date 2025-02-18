**Title: Toward a Toolkit for Analyzing Complexity in Software**

## **Introduction**
Software complexity has reached a point where it is no longer just an engineering challenge but an epistemological one. As systems grow, they become harder to observe, increasing cognitive load and making decision-making less transparent. Traditional metrics like coupling and cohesion provide partial insights, but they do not fully capture the **affordance** of a given structure—how its design influences understanding, modification, and usability over time.

This document outlines an approach to analyzing complexity in software, starting with **proximity mapping** and progressively incorporating additional dimensions such as affordance aggregation, cognitive friction, and complexity compression. The goal is to conceptualize a toolkit that helps **visualize and quantify software complexity** while allowing room for discovery and refinement.

## **Core Observations & Problem Space**
1. **Proximity & Distance in Code**
   - Cohesion and coupling are not just conceptual but also **spatial** (distance between related functions, variables, or modules).
   - **SRP vs. Physical Distance** – A function may adhere to the Single Responsibility Principle (SRP) but still be difficult to use if related logic is scattered across files or folders.
   - **Semantic Proximity Mapping** – Tracking occurrences of **similar words** (including comments, function names, variables) across a codebase may reveal hidden cohesion issues.

2. **Affordance & Complexity Management**
   - Code affordance is influenced by how **readable, discoverable, and predictable** a structure is.
   - **Affordance leakage** happens when hidden dependencies or excessive abstraction increase cognitive burden.
   - **Affordance Aggregation** – Side effects, operator overloading, inheritance, and certain forms of coupling introduce hidden complexity that is not always reflected in traditional metrics.

3. **Compression & Cognitive Load**
   - **Semantic Compression** (inspired by Muratori's perspective) suggests continuously refining code to reduce redundancy without losing meaning.
   - **Programming Keyword to Symbol Ratio** – A high ratio of keywords (e.g., control structures) vs. domain symbols (e.g., function names) may indicate structural overhead.
   - **Declarative vs. Imperative Balance** – Code structure influences ease of reasoning; excessive boilerplate reduces affordance.

4. **Coupling & Its Hidden Effects**
   - Not all coupling is equal; we need better **qualitative distinctions** between "necessary" vs. "harmful" coupling.
   - **Temporal Analysis of Coupling** – Measuring how dependencies evolve over time can provide insights into growing complexity.
   - **Mapping Affordance Impact of Coupling** – Some forms of coupling limit future changes more than others.

## **Roadmap Toward a Toolkit**
### **Phase 1: Proximity Mapping (Initial Exploration)**
- **Extract & Tokenize Words** from source code (including comments, identifiers, function names, etc.).
- **Measure Word Proximity** – Count occurrences of words and track their relative distances within a file and across files.
- **Visualize Word Clusters** – Heatmaps or graphs showing **semantic neighborhoods** in a codebase.

### **Phase 2: Affordance Aggregation**
- **Classify Symbols & Keywords** – Differentiate between programming keywords (control structures) and symbols (identifiers, functions, class names).
- **Compute Keyword-to-Symbol Ratio** – Track trends that indicate declarative vs. imperative code.
- **Identify Hidden Complexity Patterns** – Spot side effects, operator overloading, inheritance depth, and other factors that impact affordance.

### **Phase 3: Coupling & Complexity Mapping**
- **Temporal Analysis of Coupling** – Measure how dependencies shift over time to identify increasing complexity.
- **Codebase Friction Analysis** – Locate areas where changes are difficult due to excessive coupling or distant cohesion.
- **Graph-Based Complexity Visualization** – Build a representation of how code components interact over time.

### **Phase 4: Refinement & Discovery**
- **User Feedback & Case Studies** – Apply the toolkit to real-world codebases and refine the approach.
- **Customizable Complexity Profiles** – Allow developers to define what "affordance" means in their context.
- **Explore Possible Prescriptive Insights** – Use historical complexity trends to suggest refactoring opportunities.

## **Next Steps**
- Start with a **basic parser** that extracts words, counts occurrences, and maps proximity.
- Experiment with **visualizing clusters** of conceptually related words.
- Expand into **affordance aggregation** by classifying symbols and detecting high-friction patterns.
- Iterate based on findings, refining the approach toward a **more holistic complexity analysis framework**.

---

### **Conclusion**
This roadmap provides a **30-50% structured approach** to a toolkit for analyzing software complexity. By grounding the exploration in proximity mapping and progressively layering in affordance, coupling, and temporal analysis, we can better understand **how complexity emerges and how to make it visible**. The remaining open-ended discovery will help refine the toolkit into something both **analytical and actionable**.

