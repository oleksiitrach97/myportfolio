import { useEffect, useRef } from "react";
import TagCloud from "TagCloud";

const icons: { name: string; color: string; label: string }[] = [
  { name: "python", color: "ffd43b", label: "Python" },
  { name: "pytorch", color: "ee4c2c", label: "PyTorch" },
  { name: "tensorflow", color: "ff6f00", label: "TensorFlow" },
  { name: "huggingface", color: "ffd21e", label: "Hugging Face" },
  { name: "langchain", color: "1c3c3c", label: "LangChain" },
  { name: "react", color: "61dafb", label: "React" },
  { name: "typescript", color: "3178c6", label: "TypeScript" },
  { name: "javascript", color: "f7df1e", label: "JavaScript" },
  { name: "nodedotjs", color: "5fa04e", label: "Node.js" },
  { name: "fastapi", color: "009688", label: "FastAPI" },
  { name: "docker", color: "2496ed", label: "Docker" },
  { name: "kubernetes", color: "326ce5", label: "Kubernetes" },
  { name: "git", color: "f05032", label: "Git" },
  { name: "github", color: "ffffff", label: "GitHub" },
  { name: "postgresql", color: "4169e1", label: "PostgreSQL" },
  { name: "mongodb", color: "47a248", label: "MongoDB" },
  { name: "redis", color: "ff4438", label: "Redis" },
  { name: "googlecloud", color: "4285f4", label: "Google Cloud" },
  { name: "vercel", color: "ffffff", label: "Vercel" },
  { name: "nextdotjs", color: "ffffff", label: "Next.js" },
  { name: "tailwindcss", color: "06b6d4", label: "Tailwind CSS" },
  { name: "nvidia", color: "76b900", label: "NVIDIA" },
];

export default function SkillSphere() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;
    const el = containerRef.current;
    el.innerHTML = "";

    const items = icons.map(
      (i) =>
        `<span class="skill-icon" data-label="${i.label}" title="${i.label}" style="display:inline-flex;align-items:center;justify-content:center;cursor:pointer;position:relative;padding:10px 12px;border-radius:9999px;background:linear-gradient(135deg, rgba(99,102,241,0.18), rgba(168,85,247,0.14));box-shadow:0 20px 50px rgba(79,70,229,0.1), inset 0 0 0 1px rgba(255,255,255,0.14);backdrop-filter:blur(10px);transition:transform 220ms ease, box-shadow 220ms ease;">
          <img src="https://cdn.simpleicons.org/${i.name}/${i.color}" alt="${i.label}" title="${i.label}" style="width:44px;height:44px;border-radius:50%;background:rgba(255,255,255,0.16);padding:8px;filter:drop-shadow(0 18px 30px rgba(168,85,247,0.22));pointer-events:none;" />
          <span class="skill-label" style="position:absolute;bottom:-32px;left:50%;transform:translateX(-50%) translateY(10px);opacity:0;pointer-events:none;padding:4px 10px;border-radius:9999px;background:rgba(15,23,42,0.9);color:#ffffff;font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;white-space:nowrap;transition:opacity 180ms ease,transform 180ms ease;filter:drop-shadow(0 12px 30px rgba(15,23,42,0.25));">${i.label}</span>
        </span>`,
    );

    const tc = TagCloud(el, items, {
      radius: 180,
      maxSpeed: "normal",
      initSpeed: "normal",
      keep: true,
      useContainerInlineStyles: false,
      useHTML: true,
    } as Parameters<typeof TagCloud>[2]);

    return () => {
      try {
        const t = tc as unknown as { destroy?: () => void };
        t?.destroy?.();
      } catch (error) {
        console.warn("Unable to destroy skill cloud", error);
      }
      el.innerHTML = "";
    };
  }, []);

  return (
    <>
      <style>{`
        .skill-icon:hover .skill-label,
        .skill-icon:focus-within .skill-label {
          opacity: 1;
          transform: translateX(-50%) translateY(0);
        }
        .skill-icon:hover,
        .skill-icon:focus-within {
          transform: translateY(-2px);
          box-shadow: 0 22px 50px rgba(79,70,229,0.18), inset 0 0 0 1px rgba(255,255,255,0.2);
        }
      `}</style>
      <div className="relative flex items-center justify-center">
        <div className="absolute inset-0 -z-10 rounded-full bg-[radial-gradient(circle_at_center,oklch(0.45_0.18_295/0.25),transparent_60%)] blur-2xl" />
        <div
          ref={containerRef}
          className="[&_.tagcloud]:!text-foreground [&_.tagcloud--item]:cursor-pointer [&_img]:transition-transform"
          style={{ width: 420, height: 420 }}
        />
      </div>
    </>
  );
}
